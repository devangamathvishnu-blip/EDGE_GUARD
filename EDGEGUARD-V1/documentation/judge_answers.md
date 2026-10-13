# Judge / Viva Quick Answers

**What is EDGEGUARD?**
An intelligent edge monitoring and protection prototype for a DC motor.

**Which sensors?**
LM35 for temperature, INA219 for voltage/current, MPU6050 for vibration.

**Why ESP32?**
It provides processing, GPIO, ADC, I2C and Wi-Fi in one platform.

**Risk formula?**
R = 0.4 RT + 0.3 RC + 0.3 RV.

**What does ML do?**
Isolation Forest detects unusual operating patterns using temperature, voltage, current and vibration.

**Does ML control the relay?**
No. ESP32 local safety logic remains authoritative.

**How many samples?**
257 samples were recorded in the documented collection run.

**Independent test set?**
No independent time-separated validation set was confirmed.

**False-alarm rate?**
No verified false-alarm rate was measured.

**EMT connection?**
Motor electromagnetic force, back EMF, inductive switching, EMI, current sensing, grounding and wireless communication.

**Why high starting current?**
At zero speed, back EMF is approximately zero, so starting current is high. As speed increases, back EMF increases and current falls.

**Wi-Fi failure?**
Basic protection remains local to the ESP32.

**Does ML predict failure?**
No. The current ML layer detects anomalous patterns; it is not a guaranteed failure predictor or exact RUL model.
