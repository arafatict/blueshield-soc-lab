# Detection engineering

Rules live in `rules/rules.yml`. Each rule links an event condition to severity, confidence, MITRE ATT&CK metadata and response guidance.

The tests verify both positive detections and a normal baseline. This is important because a rule that alerts on every event is not useful to an analyst.

The failed-logon rule uses a five-event threshold in a ten-minute window. The other examples demonstrate exact event-type, process-name and command-line matching.
