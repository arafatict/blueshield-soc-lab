from .investigation import investigation_notes
from .models import Alert

def markdown_report(alert: Alert) -> str:
    return investigation_notes(alert) + "\n## Analyst conclusion\n\nThis report documents a synthetic lab scenario; no real system was accessed.\n"
