import argparse,json
from .generator import scenario
from .normalizer import normalize_lines
from .detections import detect
from .reporting import markdown_report

def main():
 p=argparse.ArgumentParser(prog='blueshield');sub=p.add_subparsers(dest='command',required=True)
 g=sub.add_parser('generate');g.add_argument('--scenario',choices=['failed-logins','suspicious-powershell','local-account','service-created','normal'],required=True)
 d=sub.add_parser('detect');d.add_argument('--scenario',choices=['failed-logins','suspicious-powershell','local-account','service-created','normal'],required=True)
 r=sub.add_parser('report');r.add_argument('--scenario',choices=['failed-logins','suspicious-powershell','local-account','service-created'],required=True)
 a=p.parse_args();events=scenario(a.scenario)
 if a.command=='generate': print(json.dumps(events,indent=2))
 else:
  alerts=detect(normalize_lines(events))
  if a.command=='detect': print(json.dumps([x.to_dict() for x in alerts],indent=2))
  else:
   if not alerts: raise SystemExit('No alert generated for scenario')
   print(markdown_report(alerts[0]))
if __name__=='__main__': main()
