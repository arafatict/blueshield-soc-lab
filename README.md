# BlueShield SOC Lab

A reproducible Blue Team / SOC learning lab that models the defensive workflow from synthetic Windows security telemetry to alert investigation and incident documentation.

> **Safety and scope:** This project uses controlled synthetic events only. It does not attack real systems, collect credentials, execute suspicious commands, or represent incidents from a real employer or customer.

## Live showcase

https://arafatict.github.io/blueshield-soc-lab/

The showcase is a static presentation layer. It is not a real SIEM or production backend.

## Repository workflow

```text
Synthetic Windows/Sysmon-style telemetry
        ↓
Event normalization
        ↓
YAML detection rules
        ↓
Alert with severity and confidence
        ↓
Evidence timeline and triage
        ↓
MITRE ATT&CK mapping
        ↓
Containment/remediation recommendation
        ↓
Incident report
```

## What the project demonstrates

- Windows Security and Sysmon-style event modelling
- JSON/JSONL telemetry handling
- Event normalization into a common schema
- Threshold and field-based detection logic
- Sigma-inspired YAML detection rules
- Alert severity and confidence
- Evidence collection and timeline reconstruction
- MITRE ATT&CK mapping
- Defensive triage and response recommendations
- Incident report generation
- Automated tests and GitHub Actions
- Security-conscious documentation and explicit simulation boundaries

## Detection scenarios

| Scenario | Rule | ATT&CK mapping | Demonstration |
|---|---|---|---|
| Repeated failed logons | `BS-AUTH-001` | `T1110` — Brute Force | Five or more failed logons in a ten-minute window |
| Suspicious PowerShell | `BS-PS-001` | `T1059.001` — PowerShell | Synthetic process event containing an encoded-command marker |
| Local account creation | `BS-ACC-001` | `T1136.001` — Create Account: Local Account | Account-change review and access validation |
| Windows service creation | `BS-SVC-001` | `T1543.003` — Windows Service | Service-change and persistence-oriented triage |
| Normal baseline | No alert | N/A | False-positive comparison against normal activity |

All event fixtures include `simulation: true`.

## Technologies

- Python 3.11+
- PyYAML
- pytest
- JSON and JSON Lines
- YAML detection rules
- Mermaid diagrams
- Markdown incident reports
- Static HTML/CSS showcase
- GitHub Actions

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e . pytest
pytest -q
```

Run the CLI:

```bash
blueshield generate --scenario failed-logins
blueshield detect --scenario failed-logins
blueshield report --scenario failed-logins
```

Available scenarios:

```text
failed-logins
suspicious-powershell
local-account
service-created
normal
```

## Investigation output

Reports contain:

- Alert title, severity and confidence
- Host and user context
- Evidence events and timestamps
- MITRE ATT&CK mapping
- Triage guidance
- Containment recommendation
- Remediation recommendation
- Explicit synthetic-data statement

## Repository structure

```text
src/blueshield/       Core models, generator, normalizer, detections and reports
rules/                YAML detection rules
data/                 Synthetic telemetry and event schema
docs/                 Architecture, methodology, telemetry and hardening notes
cases/                Case structure guidance
reports/              Example report location
showcase/             Static GitHub Pages presentation
tests/                Automated unit and behavior tests
configs/              Safe reference-only Sysmon fragment
.github/workflows/    Automated test workflow
```

## Defensive methodology

1. Validate the alert and confirm its source.
2. Identify host, account, timestamp and event type.
3. Reconstruct a timeline from evidence.
4. Map the behavior only when the rule supports the mapping.
5. Consider expected administrative activity and false positives.
6. Recommend safe containment and remediation.
7. Document evidence, uncertainty and next investigative steps.

## Limitations

This is a portfolio and learning simulation, not a production SOC or SIEM. It does not collect live Windows telemetry, provide authentication, store shared cases, execute suspicious commands or perform containment actions.

A production implementation would require an approved endpoint telemetry source, a collector, a SIEM or database, authentication and authorization, retention controls, audit logging, notification workflows, access protection and formal incident-handling processes.

## Safety notes

- IP addresses use documentation ranges such as `192.0.2.0/24`.
- Usernames and hostnames are synthetic lab identifiers.
- The PowerShell command line is inert text; it is never executed.
- No passwords, API keys, tokens or credentials are included.
- The Sysmon XML file is reference-only and is not automatically installed or executed.

## Troubleshooting

- Use Python 3.11 or newer.
- Install the project in editable mode before using the `blueshield` command.
- Run `pytest -q` after changes.
- If detection rules cannot be loaded, run commands from the repository root and check that `rules/rules.yml` exists.
- Remove generated local outputs before repeating a manual run if you want a clean workspace.

## Author

Md Arafat Hossain — [GitHub](https://github.com/arafatict) · [Portfolio](https://arafatict.github.io/)
