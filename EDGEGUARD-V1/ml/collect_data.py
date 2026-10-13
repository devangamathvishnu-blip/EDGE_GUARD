import time
import requests
import pandas as pd

ESP32_URL = "http://10.79.77.21/api/data"
OUTPUT_FILE = "edgeguard_normal_data.csv"
COLLECTION_TIME = 300
SAMPLE_INTERVAL = 1

rows = []
start = time.time()

while time.time() - start < COLLECTION_TIME:
    try:
        data = requests.get(ESP32_URL, timeout=5).json()
        rows.append({
            "timestamp": time.time(),
            "temperature": data.get("temperature", 0),
            "voltage": data.get("voltage", 0),
            "current": data.get("current", 0),
            "vibration": data.get("vibration", 0),
            "risk": data.get("risk", 0),
            "status": data.get("status", "UNKNOWN")
        })
        print("Samples:", len(rows), data)
    except Exception as e:
        print("Collection error:", e)
    time.sleep(SAMPLE_INTERVAL)

pd.DataFrame(rows).to_csv(OUTPUT_FILE, index=False)
print(f"Saved {len(rows)} samples to {OUTPUT_FILE}")
