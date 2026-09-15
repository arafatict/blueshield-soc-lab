# Windows and Sysmon telemetry model

The lab uses synthetic events shaped like useful Windows/Sysmon signals. It does not install Sysmon or collect a real endpoint.

Useful event families represented:

- Security Event 4625: failed logon
- Security Event 4720: local account creation
- System Event 7045: service creation
- Sysmon Event 1: process creation

The `simulation: true` field is mandatory in lab fixtures so simulated evidence cannot be confused with production telemetry.

A production deployment would require an approved endpoint, Sysmon configuration, collection agent, retention policy and access controls.
