import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

INPUT_FILE = "edgeguard_normal_data.csv"
MODEL_FILE = "edgeguard_model.pkl"
FEATURES = ["temperature", "voltage", "current", "vibration"]

df = pd.read_csv(INPUT_FILE)
df = df.replace([np.inf, -np.inf], np.nan).dropna()
X = df[FEATURES]

model = Pipeline([
    ("scaler", StandardScaler()),
    ("isolation_forest", IsolationForest(
        n_estimators=200,
        contamination=0.05,
        random_state=42
    ))
])

model.fit(X)
joblib.dump(model, MODEL_FILE)

pred = model.predict(X)
print("Training samples:", len(X))
print("Model saved:", MODEL_FILE)
print("Training-set normal:", int((pred == 1).sum()))
print("Training-set anomaly:", int((pred == -1).sum()))
print("These are NOT independent validation results.")
