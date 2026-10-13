from flask import Flask, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import requests
import threading
import time

app = Flask(__name__)
CORS(app)

ESP32_URL = "http://10.79.77.21/api/data"
model = joblib.load("edgeguard_model.pkl")

latest_data = {"ml_status": "STARTING"}

def poll():
    global latest_data
    while True:
        try:
            data = requests.get(ESP32_URL, timeout=3).json()
            X = np.array([[
                data.get("temperature", 0),
                data.get("voltage", 0),
                data.get("current", 0),
                data.get("vibration", 0)
            ]])

            p = model.predict(X)[0]
            score = float(model.decision_function(X)[0])
            prediction = "NORMAL" if p == 1 else "ANOMALY"

            # Prototype visualization metric only; not a physical health percentage.
            health = int(np.clip(50 + score * 500, 0, 100))
            condition = "STABLE" if health >= 80 else (
                "DEGRADING" if health >= 60 else "ABNORMAL"
            )

            latest_data = {
                **data,
                "prediction": prediction,
                "anomaly_score": score,
                "machine_health": health,
                "condition": condition,
                "ml_status": "ACTIVE"
            }
        except Exception as e:
            latest_data["ml_status"] = "ERROR: " + str(e)

        time.sleep(1)

@app.route("/")
def root():
    return "EDGEGUARD V1 ML SERVER"

@app.route("/api/predict")
def predict():
    return jsonify(latest_data)

if __name__ == "__main__":
    threading.Thread(target=poll, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
