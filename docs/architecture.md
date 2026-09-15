# Architecture

The lab models a defensive SOC workflow with synthetic Windows/Sysmon-style events. The generator creates controlled fixtures; the normalizer creates a common event model; the detection engine evaluates YAML rules; the investigator creates evidence and reports.

No real endpoint, credential, network target or customer data is used.
