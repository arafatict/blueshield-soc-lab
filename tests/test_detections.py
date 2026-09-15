from blueshield.generator import scenario
from blueshield.normalizer import normalize_lines
from blueshield.detections import detect


def test_failed_logon_burst_creates_high_alert():
    alerts = detect(normalize_lines(scenario("failed-logins")))
    assert len(alerts) == 1
    assert alerts[0].rule_id == "BS-AUTH-001"
    assert alerts[0].severity == "high"
    assert alerts[0].mitre_technique_id == "T1110"


def test_normal_activity_does_not_alert():
    assert detect(normalize_lines(scenario("normal"))) == []


def test_suspicious_powershell_is_detected():
    alerts = detect(normalize_lines(scenario("suspicious-powershell")))
    assert alerts[0].rule_id == "BS-PS-001"
