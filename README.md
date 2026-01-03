 ML-Enabled WAF Anomaly Detection Module

 1. Problem Statement

Traditional Web Application Firewalls (WAFs) rely on fixed, rule-based signatures. These rules fail to detect **new / zero-day attacks**, bot abuse, and unusual behavior patterns. This project builds a **Machine Learning (ML) based anomaly detection module** that learns normal traffic behavior and flags deviations automatically. The module is designed for **future integration with an existing WAF**.



 2. Objective

* Learn normal web/network traffic patterns (baseline)
* Detect anomalies using Machine Learning
* Reduce false positives compared to static rules
* Provide explainable alerts for administrators

3. System Architecture

* Traffic Data (simulated web requests)
* ML Anomaly Detection Engine (Isolation Forest)
* Flask Backend API
* Web Dashboard (HTML)

**Flow**: Traffic Data → ML Model → Anomaly Detection → Flask Server → Dashboard

4. Technology Used

* **Python 3**
* **Scikit-learn** – Isolation Forest (unsupervised ML)
* **NumPy / Pandas** – Data handling
* **Flask** – Local dashboard (localhost)



5. Project Structure

ML_WAF_Project/
│
├── anomaly_detector.py      # Core ML anomaly detection logic
├── app.py                   # Flask dashboard (localhost)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```



6. How It Works

1. Network traffic features are collected (request rate, packet size, duration, etc.)
2. ML model learns **normal traffic baseline**
3. Incoming traffic is compared with the baseline
4. If deviation is high → **Anomaly detected**
5. Output can later be converted into WAF security rules



7. How to Run the Project

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run anomaly detection

```bash
python anomaly_detector.py
```

### Step 3: Run dashboard (optional)

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## Sample Output

* ✅ Normal traffic detected
* 🚨 Anomaly detected for unusual traffic spikes

This demonstrates ML-based detection without predefined rules.


## 🔐 Deployment Note

Currently deployed on **localhost** for testing and demonstration. The module can be deployed on:

* On-premise servers
* Private cloud
* Secure defense networks

---

## 🚀 Future Enhancements

* Integration with real WAF (ModSecurity)
* Real-time traffic capture
* Automated rule generation
* Advanced visualization dashboard

---

## 📽️ Demo

A 5-minute demo video demonstrates:

* Anomaly detection
* Dashboard output
* ML-based decision making

---

## 👩‍💻 Author

Developed for **SWAVLAMBAN 2025 – Challenge 3**
Naval Innovathon 2025


