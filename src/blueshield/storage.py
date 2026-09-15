import json
from pathlib import Path
from .models import Alert

def save_alerts(alerts, path):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps([a.to_dict() for a in alerts],indent=2))

def load_alerts(path): return json.loads(Path(path).read_text()) if Path(path).exists() else []
