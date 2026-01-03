from flask import Flask, render_template
import pandas as pd
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Load data
data = pd.read_csv("traffic.csv")

# Train model
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(data)

# Predict
data["result"] = model.predict(data)

@app.route("/")
def dashboard():
    return render_template("index.html", tables=data.values.tolist())

if __name__ == "__main__":
    app.run(debug=True)
