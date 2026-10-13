# EDGEGUARD V1

**Intelligent Edge Monitoring & Protection System for Motor Safety**

EDGEGUARD V1 is a prototype motor monitoring and protection system built around ESP32.

## Architecture

Sensors -> ESP32 local safety engine -> HTTP telemetry -> Dashboard
                                      -> Python ML anomaly detector

### Sensors
- LM35: temperature, GPIO34
- INA219: voltage/current, I2C
- MPU6050: vibration, I2C

### Actuation
- Relay: GPIO27
- L298N ENB: GPIO25
- L298N IN3: GPIO26
- L298N IN4: GPIO32
- Buzzer: GPIO33
- Green/Yellow/Red LEDs: GPIO4/13/14

### Risk model
R = 0.4*TemperatureRisk + 0.3*CurrentRisk + 0.3*VibrationRisk

NORMAL < 40
WARNING = 40 to <70
CRITICAL >= 70

These weights and thresholds are prototype design choices, not universal standards.

### ML
Isolation Forest using:
1. temperature
2. voltage
3. current
4. vibration

The ML layer is advisory. The ESP32 remains the local protection authority and ML does not directly control the relay.

### Recorded data
The documented collection run contained **257 samples**. The available record does not establish that every sample was an independently verified normal running-motor sample, so this repository does not claim a validated accuracy or false-alarm percentage.

### Hackathon
- Project: EDGEGUARD V1
- Team: InnoVolt
- Domain: Smart Infrastructure and Industrial Automation
- Event: NAVYANTRA 24-hour Hardware Hackathon, KSSEM, Bengaluru
