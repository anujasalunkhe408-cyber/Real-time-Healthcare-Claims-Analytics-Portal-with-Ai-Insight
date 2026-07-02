import json
import os
from datetime import datetime

from email_templates import EmailTemplates


# ==========================================
# Save Email Log
# ==========================================

def save_email_log(patient_name, claim_id, email, status):

    log_file = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "email_logs.json"
    )

    log = {
        "patient_name": patient_name,
        "claim_id": claim_id,
        "email": email,
        "status": status,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "time": datetime.now().strftime("%H:%M:%S")
    }

    try:

        with open(log_file, "r") as file:

            logs = json.load(file)

    except:

        logs = []

    logs.append(log)

    with open(log_file, "w") as file:

        json.dump(logs, file, indent=4)


# ==========================================
# Send Status Update Email
# ==========================================

def send_status_update_email(patient_name,
                             claim_id,
                             email,
                             current_status):

    subject, body = EmailTemplates.status_update_email(

        patient_name,

        claim_id,

        current_status

    )

    print("=" * 70)
    print("STATUS UPDATE EMAIL")
    print("=" * 70)

    print("To      :", email)

    print("Subject :", subject)

    print(body)

    print("=" * 70)

    print("Status Update Email Sent Successfully")

    save_email_log(

        patient_name,

        claim_id,

        email,

        current_status

    )


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    send_status_update_email(

        patient_name="Rahul Sharma",

        claim_id="C1015",

        email="rahul@gmail.com",

        current_status="Pending Verification"

    )