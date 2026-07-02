import pandas as pd
import json
import os
from datetime import datetime

# ==========================================
# File Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")

os.makedirs(DATA_FOLDER, exist_ok=True)

CLAIMS_FILE = os.path.join(DATA_FOLDER, "claims.csv")

FOLLOWUP_FILE = os.path.join(
    DATA_FOLDER,
    "followup_alerts.json"
)

# ==========================================
# Generate Follow-up Alerts
# ==========================================

def generate_followup_alerts():

    df = pd.read_csv(CLAIMS_FILE)

    today = datetime.now()

    alerts = []

    print("=" * 75)
    print("FOLLOW-UP ALERTS")
    print("=" * 75)

    for _, row in df.iterrows():

        due_date = datetime.strptime(
            row["Due_Date"],
            "%d-%m-%Y"
        )

        # Pending claim whose deadline has passed
        if (
            row["Claim_Status"] == "Pending"
            and due_date < today
        ):

            overdue_days = (today - due_date).days

            alert = {

                "followup_id": f"FU{len(alerts)+1:03}",

                "claim_id": row["Claim_ID"],

                "patient_id": row["Patient_ID"],

                "patient_name": row["Patient_Name"],

                "email": row["Email"],

                "due_date": row["Due_Date"],

                "overdue_days": overdue_days,

                "message": "Follow-up required for pending healthcare claim.",

                "status": "Follow-up Pending",

                "date": today.strftime("%d-%m-%Y"),

                "time": today.strftime("%H:%M:%S")

            }

            alerts.append(alert)

            print(f"""
Follow-up ID : {alert['followup_id']}

Claim ID     : {row['Claim_ID']}

Patient      : {row['Patient_Name']}

Email        : {row['Email']}

Due Date     : {row['Due_Date']}

Overdue Days : {overdue_days}

Status       : Follow-up Pending

------------------------------------------------------------
""")

    with open(FOLLOWUP_FILE, "w") as file:

        json.dump(alerts, file, indent=4)

    print("=" * 75)

    print("Total Follow-up Alerts :", len(alerts))

    print("=" * 75)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    generate_followup_alerts()