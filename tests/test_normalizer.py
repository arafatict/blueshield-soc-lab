from blueshield.generator import scenario
from blueshield.normalizer import normalize

def test_normalizer_creates_common_event_model():
    event = normalize(scenario('failed-logins')[0])
    assert event.event_id == '4625'
    assert event.event_type == 'authentication_failure'
    assert event.simulation is True
    assert event.host == 'LAB-WIN10-01'
