import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("traffic.csv")

model = IsolationForest(contamination=0.3)
model.fit(data)

data["anomaly"] = model.predict(data)

for i, row in data.iterrows():
    if row["anomaly"] == -1:
        print("🚨 Anomaly detected:", row.values)
    else:
        print("✅ Normal traffic:", row.values)
