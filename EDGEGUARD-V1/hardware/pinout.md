# EDGEGUARD V1 Pinout

| GPIO | Device |
|---|---|
| 34 | LM35 analog output |
| 21 | I2C SDA - INA219 + MPU6050 |
| 22 | I2C SCL - INA219 + MPU6050 |
| 27 | Relay |
| 25 | L298N ENB |
| 26 | L298N IN3 |
| 32 | L298N IN4 |
| 33 | Buzzer |
| 4 | Green LED |
| 13 | Yellow LED |
| 14 | Red LED |
| 35 | Manual fault button |

GPIO35 is input-only. The documented prototype used an external 10k pull-up to 3.3V and a button to GND.
