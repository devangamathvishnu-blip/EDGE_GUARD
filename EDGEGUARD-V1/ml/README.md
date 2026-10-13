# ML Service

ESP32 `/api/data` -> collector -> CSV -> StandardScaler + IsolationForest -> Flask `/api/predict`

Install:
```bash
py -m pip install -r requirements.txt
```

Train:
```bash
py train_model.py
```

Run:
```bash
py ml_server.py
```

Open:
`http://localhost:5000/api/predict`

The ML model is an unsupervised anomaly detector. Training-set predictions are not independent validation and contamination=0.05 is not a measured false-alarm rate.
