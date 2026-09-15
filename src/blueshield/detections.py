from datetime import datetime, timedelta, timezone
from pathlib import Path
import yaml
from .models import Alert, Event

def _rules():
    return yaml.safe_load((Path(__file__).parents[2] / "rules" / "rules.yml").read_text())

def _dt(value): return datetime.fromisoformat(value.replace("Z", "+00:00"))

def detect(events: list[Event]) -> list[Alert]:
    alerts=[]
    for rule in _rules():
        matching=[e for e in events if e.event_type==rule.get("event_type") and (not rule.get("process_name") or e.process_name.lower()==rule["process_name"].lower()) and (not rule.get("command_contains") or rule["command_contains"].lower() in e.command_line.lower())]
        if rule.get("threshold_count"):
            groups={}
            for e in matching: groups.setdefault((e.host,e.user),[]).append(e)
            for (host,user),group in groups.items():
                group.sort(key=lambda x:_dt(x.timestamp)); window=rule["window_minutes"]
                for i,e in enumerate(group):
                    evidence=[x for x in group if _dt(x.timestamp)>=_dt(e.timestamp) and _dt(x.timestamp)<=_dt(e.timestamp)+timedelta(minutes=window)]
                    if len(evidence)>=rule["threshold_count"]:
                        alerts.append(_alert(rule,evidence,host,user));break
        elif matching:
            for e in matching: alerts.append(_alert(rule,[e],e.host,e.user))
    return alerts

def _alert(rule,evidence,host,user):
    return Alert(alert_id=f"BS-ALERT-{len(evidence):04d}-{rule['id']}",rule_id=rule['id'],title=rule['title'],severity=rule['severity'],confidence=rule['confidence'],timestamp=evidence[-1].timestamp,host=host,user=user,evidence=[e.to_dict() for e in evidence],mitre_technique_id=rule['mitre_technique_id'],mitre_technique_name=rule['mitre_technique_name'],containment_recommendation=rule['containment'],remediation_recommendation=rule['remediation'])
