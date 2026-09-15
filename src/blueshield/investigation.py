from .models import Alert

def timeline(alert: Alert):
    return sorted(alert.evidence,key=lambda x:x.get('timestamp',''))

def investigation_notes(alert: Alert):
    return f"""# Investigation: {alert.alert_id}

- **Title:** {alert.title}
- **Severity:** {alert.severity}
- **Confidence:** {alert.confidence}
- **Host:** {alert.host}
- **User:** {alert.user or 'Not present'}
- **MITRE ATT&CK:** {alert.mitre_technique_id} — {alert.mitre_technique_name}
- **Simulation:** Evidence is synthetic and controlled for this learning lab.

## Evidence

""" + "\n".join(f"- `{e.get('timestamp')}` Event {e.get('event_id')} {e.get('event_type')}" for e in timeline(alert)) + f"""

## Triage

Review the evidence, confirm whether the activity is expected, and preserve related events before deciding on response.

## Containment recommendation

{alert.containment_recommendation}

## Remediation recommendation

{alert.remediation_recommendation}
"""
