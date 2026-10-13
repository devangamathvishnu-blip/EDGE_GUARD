# Methodology

1. Acquire temperature, current, voltage and vibration.
2. Process readings locally on ESP32.
3. Calculate normalized temperature/current/vibration risk.
4. Calculate weighted overall risk.
5. Classify NORMAL, WARNING or CRITICAL.
6. On CRITICAL, activate local protection.
7. Publish telemetry through ESP32 HTTP API.
8. Dashboard displays live information.
9. Python Isolation Forest provides additional anomaly detection.

Protection is local; dashboard and ML are supervisory layers.
