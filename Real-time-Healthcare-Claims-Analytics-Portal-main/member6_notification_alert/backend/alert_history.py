import json
import os

# ==========================================
# File Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")

os.makedirs(DATA_FOLDER, exist_ok=True)

ALERT_FILE = os.path.join(DATA_FOLDER, "alerts.json")

NOTIFICATION_FILE = os.path.join(
    DATA_FOLDER,
    "admin_notifications.json"
)

HISTORY_FILE = os.path.join(
    DATA_FOLDER,
    "alert_history.json"
)


# ==========================================
# Track Alert History
# ==========================================

def track_alert_history():

    try:

        with open(ALERT_FILE, "r") as file:

            alerts = json.load(file)

    except:

        alerts = []


    try:

        with open(NOTIFICATION_FILE, "r") as file:

            notifications = json.load(file)

    except:

        notifications = []


    history = []

    print("=" * 75)
    print("ALERT HISTORY")
    print("=" * 75)

    for i in range(len(alerts)):

        alert = alerts[i]

        notification = {}

        if i < len(notifications):

            notification = notifications[i]

        record = {

            "history_id": f"H{i+1:03}",

            "claim_id": alert.get("claim_id", ""),

            "patient_id": alert.get("patient_id", ""),

            "hospital_id": alert.get("hospital_id", ""),

            "alert": alert.get(
                "alert",
                "Fraud Alert"
            ),

            "priority": notification.get(
                "priority",
                "HIGH"
            ),

            "notification_status": notification.get(
                "status",
                "Unread"
            ),

            "date": alert.get("date", ""),

            "time": alert.get("time", "")

        }

        history.append(record)

        print(f"""
History ID          : {record['history_id']}

Claim ID            : {record['claim_id']}

Patient ID          : {record['patient_id']}

Hospital ID         : {record['hospital_id']}

Alert               : {record['alert']}

Priority            : {record['priority']}

Notification Status : {record['notification_status']}

Date                : {record['date']}

Time                : {record['time']}

------------------------------------------------------------
""")

    with open(HISTORY_FILE, "w") as file:

        json.dump(history, file, indent=4)

    print("=" * 75)

    print("Total Alert History Records :", len(history))

    print("=" * 75)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    track_alert_history()