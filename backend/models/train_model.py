import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv("../data/metrics.csv")
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)
joblib.dump(model, "anomaly_model.pkl")
print("Model trained and saved")
