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

REMINDER_FILE = os.path.join(
    DATA_FOLDER,
    "pending_reminders.json"
)

# ==========================================
# Generate Pending Claim Reminders
# ==========================================

def generate_pending_reminders():

    df = pd.read_csv(CLAIMS_FILE)

    pending_claims = df[df["Claim_Status"] == "Pending"]

    reminders = []

    print("=" * 75)
    print("PENDING CLAIM REMINDERS")
    print("=" * 75)

    if pending_claims.empty:

        print("\nNo Pending Claims Found.\n")

    else:

        for index, row in pending_claims.iterrows():

            reminder = {

                "reminder_id": f"PR{len(reminders)+1:03}",

                "claim_id": row["Claim_ID"],

                "patient_id": row["Patient_ID"],

                "patient_name": row["Patient_Name"],

                "email": row["Email"],

                "message": "Your healthcare claim is still pending. Please complete the required process.",

                "status": "Reminder Sent",

                "date": datetime.now().strftime("%d-%m-%Y"),

                "time": datetime.now().strftime("%H:%M:%S")

            }

            reminders.append(reminder)

            print(f"""
Reminder ID  : {reminder['reminder_id']}

Claim ID     : {row['Claim_ID']}

Patient      : {row['Patient_Name']}

Email        : {row['Email']}

Status       : Pending

Message      : Reminder Sent Successfully

------------------------------------------------------------
""")

    with open(REMINDER_FILE, "w") as file:

        json.dump(reminders, file, indent=4)

    print("=" * 75)

    print("Total Pending Reminders :", len(reminders))

    print("=" * 75)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    generate_pending_reminders()