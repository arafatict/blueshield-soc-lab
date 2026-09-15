from .models import Event

def normalize(raw: dict) -> Event:
    return Event(
      event_id=str(raw.get("event_id", raw.get("EventID", "unknown"))),
      event_type=str(raw.get("event_type", "unknown")), provider=str(raw.get("provider", "synthetic")),
      timestamp=str(raw.get("timestamp", "")), host=str(raw.get("host", "unknown")),
      user=str(raw.get("user", "")), source_ip=str(raw.get("source_ip", "")),
      process_name=str(raw.get("process_name", "")), command_line=str(raw.get("command_line", "")),
      target=str(raw.get("target", "")), simulation=bool(raw.get("simulation", True)), raw=raw)

def normalize_lines(lines):
    return [normalize(line) for line in lines if line]
