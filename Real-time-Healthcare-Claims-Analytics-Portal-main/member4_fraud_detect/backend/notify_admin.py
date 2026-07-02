import json
import os
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))

notification = {
    "title": "🚨 Fraud Claim Detected",
    "message": "A high-risk healthcare claim requires immediate review.",
    "claim_id": "C0015",
    "risk_score": 90,
    "status": "High Risk",
    "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
}

# Save for frontend
data_folder = os.path.join(base_dir, "..", "frontend", "data")
os.makedirs(data_folder, exist_ok=True)

notification_file = os.path.join(data_folder, "admin_notification.json")

with open(notification_file, "w") as file:
    json.dump(notification, file, indent=4)

print("Administrator notification generated successfully.")