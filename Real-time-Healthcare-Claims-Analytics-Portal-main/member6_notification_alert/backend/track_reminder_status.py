import json
import os
from datetime import datetime

# ==========================================
# File Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")

os.makedirs(DATA_FOLDER, exist_ok=True)

PENDING_FILE = os.path.join(DATA_FOLDER, "pending_reminders.json")

DEADLINE_FILE = os.path.join(DATA_FOLDER, "deadline_reminders.json")

FOLLOWUP_FILE = os.path.join(DATA_FOLDER, "followup_alerts.json")

STATUS_FILE = os.path.join(DATA_FOLDER, "reminder_status.json")


# ==========================================
# Read JSON File
# ==========================================

def read_json(file_path):

    try:

        with open(file_path, "r") as file:

            return json.load(file)

    except:

        return []


# ==========================================
# Track Reminder Status
# ==========================================

def track_reminder_status():

    pending = read_json(PENDING_FILE)

    deadline = read_json(DEADLINE_FILE)

    followup = read_json(FOLLOWUP_FILE)

    reminder_history = []

    print("=" * 70)
    print("REMINDER STATUS")
    print("=" * 70)

    reminder_id = 1

    for reminder in pending:

        reminder_history.append({

            "status_id": f"RS{reminder_id:03}",

            "claim_id": reminder["claim_id"],

            "type": "Pending Reminder",

            "status": "Sent",

            "date": datetime.now().strftime("%d-%m-%Y"),

            "time": datetime.now().strftime("%H:%M:%S")

        })

        reminder_id += 1


    for reminder in deadline:

        reminder_history.append({

            "status_id": f"RS{reminder_id:03}",

            "claim_id": reminder["claim_id"],

            "type": "Deadline Reminder",

            "status": "Sent",

            "date": datetime.now().strftime("%d-%m-%Y"),

            "time": datetime.now().strftime("%H:%M:%S")

        })

        reminder_id += 1


    for reminder in followup:

        reminder_history.append({

            "status_id": f"RS{reminder_id:03}",

            "claim_id": reminder["claim_id"],

            "type": "Follow-up Alert",

            "status": "Pending",

            "date": datetime.now().strftime("%d-%m-%Y"),

            "time": datetime.now().strftime("%H:%M:%S")

        })

        reminder_id += 1


    with open(STATUS_FILE, "w") as file:

        json.dump(reminder_history, file, indent=4)


    for record in reminder_history:

        print(f"""

Status ID : {record['status_id']}

Claim ID  : {record['claim_id']}

Type      : {record['type']}

Status    : {record['status']}

Date      : {record['date']}

Time      : {record['time']}

--------------------------------------------------------
""")


    print("=" * 70)

    print("Total Reminder Status Records :", len(reminder_history))

    print("=" * 70)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    track_reminder_status()