from blueshield.generator import scenario
from blueshield.normalizer import normalize_lines
from blueshield.detections import detect
from blueshield.reporting import markdown_report


def test_report_contains_evidence_and_response_sections():
    report = markdown_report(detect(normalize_lines(scenario('suspicious-powershell')))[0])
    assert '## Evidence' in report
    assert '## Containment recommendation' in report
    assert '## Remediation recommendation' in report
    assert 'synthetic' in report.lower()
