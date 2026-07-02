import json
import os
from datetime import datetime

from email_templates import EmailTemplates


# ==========================================
# Email Logger
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
# Send Approval Email
# ==========================================

def send_approval_email(patient_name, claim_id, email):

    subject, body = EmailTemplates.approval_email(
        patient_name,
        claim_id
    )

    print("=" * 70)
    print("APPROVAL EMAIL")
    print("=" * 70)

    print("To      :", email)
    print("Subject :", subject)

    print(body)

    print("=" * 70)

    print("Email Sent Successfully")

    save_email_log(
        patient_name,
        claim_id,
        email,
        "Approved"
    )


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    send_approval_email(

        patient_name="Rahul Sharma",

        claim_id="C1001",

        email="rahul@gmail.com"

    )