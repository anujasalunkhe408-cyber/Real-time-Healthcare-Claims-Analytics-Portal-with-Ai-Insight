import pandas as pd
import os
import json
from datetime import datetime

# -----------------------------
# Load Dataset
# -----------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))

dataset_path = os.path.join(
    base_dir,
    "..",
    "dataset",
    "HealthcareClaims.csv"
)

df = pd.read_csv(dataset_path)

# -----------------------------
# Select High Risk Claim
# -----------------------------
high_risk = df[df["Claim_Amount"] >= 150000]

if high_risk.empty:
    print("No High Risk Claim Found.")
    exit()

claim = high_risk.iloc[0]

# -----------------------------
# Calculate Risk Score
# -----------------------------
risk_score = 90

status = "High Risk"

# -----------------------------
# Create Alert Data
# -----------------------------
alert = {

    "claim_id": claim["Claim_ID"],

    "patient_id": claim["Patient_ID"],

    "hospital_id": claim["Hospital_ID"],

    "risk_score": risk_score,

    "status": status,

    "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")

}

# -----------------------------
# Save Alert
# -----------------------------
reports_folder = os.path.join(
    base_dir,
    "..",
    "frontend",
    "data"
)

os.makedirs(reports_folder, exist_ok=True)

alert_file = os.path.join(
    reports_folder,
    "alert.json"
)

with open(alert_file, "w") as file:

    json.dump(alert, file, indent=4)

# -----------------------------
# Console Output
# -----------------------------
print("\n==============================")
print(" FRAUD ALERT GENERATED ")
print("==============================")

print("Claim ID :", alert["claim_id"])
print("Patient :", alert["patient_id"])
print("Hospital :", alert["hospital_id"])
print("Risk Score :", alert["risk_score"], "%")
print("Status :", alert["status"])

print("\nAlert saved successfully.")