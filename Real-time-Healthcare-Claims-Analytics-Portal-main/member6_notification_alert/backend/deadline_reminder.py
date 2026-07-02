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
    "deadline_reminders.json"
)

# ==========================================
# Generate Deadline Reminders
# ==========================================

def generate_deadline_reminders():

    df = pd.read_csv(CLAIMS_FILE)

    today = datetime.now()

    reminders = []

    print("=" * 75)
    print("DEADLINE REMINDERS")
    print("=" * 75)

    for _, row in df.iterrows():

        due_date = datetime.strptime(
            row["Due_Date"],
            "%d-%m-%Y"
        )

        days_left = (due_date - today).days

        if 0 <= days_left <= 3:

            reminder = {

                "reminder_id": f"DR{len(reminders)+1:03}",

                "claim_id": row["Claim_ID"],

                "patient_id": row["Patient_ID"],

                "patient_name": row["Patient_Name"],

                "email": row["Email"],

                "due_date": row["Due_Date"],

                "days_left": days_left,

                "message": f"Your healthcare claim deadline is in {days_left} day(s).",

                "date": today.strftime("%d-%m-%Y"),

                "time": today.strftime("%H:%M:%S")

            }

            reminders.append(reminder)

            print(f"""
Reminder ID : {reminder['reminder_id']}

Claim ID    : {row['Claim_ID']}

Patient     : {row['Patient_Name']}

Due Date    : {row['Due_Date']}

Days Left   : {days_left}

Message      : Deadline Reminder Sent

------------------------------------------------------------
""")

    with open(REMINDER_FILE, "w") as file:

        json.dump(reminders, file, indent=4)

    print("=" * 75)

    print("Total Deadline Reminders :", len(reminders))

    print("=" * 75)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    generate_deadline_reminders()