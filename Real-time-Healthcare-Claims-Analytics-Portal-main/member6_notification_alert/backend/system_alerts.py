import json
import os
from datetime import datetime

# ==========================================
# File Path
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")

os.makedirs(DATA_FOLDER, exist_ok=True)

SYSTEM_ALERT_FILE = os.path.join(DATA_FOLDER, "system_alerts.json")


# ==========================================
# Generate System Alerts
# ==========================================

def generate_system_alerts():

    current_date = datetime.now().strftime("%d-%m-%Y")

    current_time = datetime.now().strftime("%H:%M:%S")

    alerts = [

        {
            "alert_id": "SA001",
            "type": "Database",
            "message": "Database Connected Successfully",
            "status": "Online",
            "date": current_date,
            "time": current_time
        },

        {
            "alert_id": "SA002",
            "type": "AI Model",
            "message": "Fraud Detection Model Running",
            "status": "Running",
            "date": current_date,
            "time": current_time
        },

        {
            "alert_id": "SA003",
            "type": "Email Service",
            "message": "Email Notification Service Active",
            "status": "Online",
            "date": current_date,
            "time": current_time
        },

        {
            "alert_id": "SA004",
            "type": "Dataset",
            "message": "Healthcare Claims Dataset Loaded",
            "status": "Loaded",
            "date": current_date,
            "time": current_time
        },

        {
            "alert_id": "SA005",
            "type": "Storage",
            "message": "System Storage Available",
            "status": "Healthy",
            "date": current_date,
            "time": current_time
        }

    ]

    with open(SYSTEM_ALERT_FILE, "w") as file:

        json.dump(alerts, file, indent=4)

    print("=" * 70)

    print("SYSTEM ALERTS")

    print("=" * 70)

    for alert in alerts:

        print(f"""
Alert ID : {alert['alert_id']}

Type     : {alert['type']}

Message  : {alert['message']}

Status   : {alert['status']}

Date     : {alert['date']}

Time     : {alert['time']}
""")

    print("=" * 70)

    print("Total System Alerts :", len(alerts))

    print("=" * 70)


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    generate_system_alerts()