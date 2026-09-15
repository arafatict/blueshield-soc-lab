from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class Event:
    event_id: str
    event_type: str
    provider: str
    timestamp: str
    host: str
    user: str = ""
    source_ip: str = ""
    process_name: str = ""
    command_line: str = ""
    target: str = ""
    simulation: bool = True
    raw: dict[str, Any] | None = None
    def to_dict(self): return asdict(self)

@dataclass
class Alert:
    alert_id: str
    rule_id: str
    title: str
    severity: str
    confidence: str
    timestamp: str
    host: str
    user: str
    evidence: list[dict[str, Any]]
    mitre_technique_id: str
    mitre_technique_name: str
    status: str = "New"
    analyst_notes: str = ""
    containment_recommendation: str = ""
    remediation_recommendation: str = ""
    def to_dict(self): return asdict(self)
