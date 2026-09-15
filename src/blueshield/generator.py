from datetime import datetime, timedelta, timezone

def _ts(minutes): return (datetime(2026,1,15,9,30,tzinfo=timezone.utc)+timedelta(minutes=minutes)).isoformat().replace('+00:00','Z')

def scenario(name):
    base={"provider":"Microsoft-Windows-Synthetic-Lab","host":"LAB-WIN10-01","simulation":True}
    if name=="failed-logins": return [{**base,"event_id":"4625","event_type":"authentication_failure","timestamp":_ts(i),"user":"lab.user","source_ip":"192.0.2.25","target":"LAB-WIN10-01"} for i in range(6)]
    if name=="suspicious-powershell": return [{**base,"event_id":"1","event_type":"process_create","timestamp":_ts(0),"user":"lab.user","process_name":"powershell.exe","command_line":"powershell.exe -NoProfile -EncodedCommand SIMULATED_SAFE_VALUE"}]
    if name=="local-account": return [{**base,"event_id":"4720","event_type":"account_created","timestamp":_ts(0),"user":"lab.admin","target":"lab-temp-user"}]
    if name=="service-created": return [{**base,"event_id":"7045","event_type":"service_created","timestamp":_ts(0),"user":"lab.admin","target":"SyntheticUpdateService","command_line":"C:\\Lab\\synthetic-service.exe"}]
    if name=="normal": return [{**base,"event_id":"4624","event_type":"authentication_success","timestamp":_ts(0),"user":"lab.user","source_ip":"192.0.2.10"},{**base,"event_id":"1","event_type":"process_create","timestamp":_ts(2),"user":"lab.user","process_name":"explorer.exe","command_line":"explorer.exe"}]
    raise ValueError(f"unknown scenario: {name}")

def all_scenarios(): return {n:scenario(n) for n in ["failed-logins","suspicious-powershell","local-account","service-created","normal"]}
