import json
import os
from datetime import datetime

# ==========================================
# File Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")

os.makedirs(DATA_FOLDER, exist_ok=True)

ALERT_FILE = os.path.join(DATA_FOLDER, "alerts.json")

ADMIN_NOTIFICATION_FILE = os.path.join(
    DATA_FOLDER,
    "admin_notifications.json"
)

# ==========================================
# Notify Administrator
# ==========================================

def notify_administrator():

    try:

        with open(ALERT_FILE, "r") as file:

            alerts = json.load(file)

    except FileNotFoundError:

        print("Fraud alerts file not found.")

        return

    if len(alerts) == 0:

        print("No fraud alerts available.")

        return

    notifications = []

    print("=" * 70)
    print("ADMINISTRATOR NOTIFICATIONS")
    print("=" * 70)

    for i, alert in enumerate(alerts, start=1):

        notification = {

            "notification_id": f"N{i:03}",

            "claim_id": alert["claim_id"],

            "patient_id": alert["patient_id"],

            "hospital_id": alert["hospital_id"],

            "message": "High Risk Healthcare Claim Detected",

            "priority": "HIGH",

            "status": "Unread",

            "date": datetime.now().strftime("%d-%m-%Y"),

            "time": datetime.now().strftime("%H:%M:%S")

        }

        notifications.append(notification)

        print(f"""
Notification ID : {notification['notification_id']}

Claim ID        : {notification['claim_id']}

Patient ID      : {notification['patient_id']}

Hospital ID     : {notification['hospital_id']}

Priority        : {notification['priority']}

Status          : {notification['status']}

Message         : {notification['message']}

----------------------------------------------
""")

    with open(ADMIN_NOTIFICATION_FILE, "w") as file:

        json.dump(notifications, file, indent=4)

    print("=" * 70)
    print("Total Notifications Sent :", len(notifications))
    print("=" * 70)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    notify_administrator()