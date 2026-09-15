from blueshield.generator import scenario
from blueshield.normalizer import normalize_lines
from blueshield.detections import detect


def test_all_defensive_scenarios_create_expected_alerts():
    expected = {'local-account': 'BS-ACC-001', 'service-created': 'BS-SVC-001'}
    for name, rule_id in expected.items():
        alerts = detect(normalize_lines(scenario(name)))
        assert len(alerts) == 1
        assert alerts[0].rule_id == rule_id
        assert alerts[0].evidence[0]['simulation'] is True


def test_alert_contains_recommendations_and_mitre_mapping():
    alert = detect(normalize_lines(scenario('failed-logins')))[0]
    assert alert.containment_recommendation
    assert alert.remediation_recommendation
    assert alert.mitre_technique_id == 'T1110'
