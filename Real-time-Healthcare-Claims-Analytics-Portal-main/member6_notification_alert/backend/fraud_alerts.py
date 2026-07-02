import pandas as pd
import json
import os
from datetime import datetime


# ==========================================
# File Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.join(BASE_DIR, "..", "data", "claims.csv")

ALERT_FILE = os.path.join(BASE_DIR, "..", "data", "alerts.json")


# ==========================================
# Generate Fraud Alerts
# ==========================================

def generate_fraud_alerts():

    df = pd.read_csv(DATASET)

    fraud_claims = df[df["Fraud"] == 1]

    alerts = []

    print("=" * 70)
    print("REAL-TIME FRAUD ALERTS")
    print("=" * 70)

    if fraud_claims.empty:

        print("\nNo Fraudulent Claims Found.\n")

    else:

        for _, row in fraud_claims.iterrows():

            alert = {

                "claim_id": row["Claim_ID"],
                "patient_id": row["Patient_ID"],
                "hospital_id": row["Hospital_ID"],
                "claim_amount": int(row["Claim_Amount"]),
                "fraud": int(row["Fraud"]),
                "alert": "High Risk Claim Detected",
                "date": datetime.now().strftime("%d-%m-%Y"),
                "time": datetime.now().strftime("%H:%M:%S")

            }

            alerts.append(alert)

            print(f"""
Claim ID      : {row['Claim_ID']}
Patient ID    : {row['Patient_ID']}
Hospital ID   : {row['Hospital_ID']}
Claim Amount  : ₹{row['Claim_Amount']}
Status        : HIGH RISK
""")

    with open(ALERT_FILE, "w") as file:

        json.dump(alerts, file, indent=4)

    print("=" * 70)

    print(f"Total Alerts Generated : {len(alerts)}")

    print("=" * 70)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    generate_fraud_alerts()