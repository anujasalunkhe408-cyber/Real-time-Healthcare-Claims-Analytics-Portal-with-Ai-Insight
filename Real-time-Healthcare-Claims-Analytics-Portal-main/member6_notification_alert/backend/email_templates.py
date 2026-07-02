# ==========================================
# Email Templates
# Project: Notifications & Alerts Module
# ==========================================

class EmailTemplates:

    # --------------------------------------
    # Approval Email
    # --------------------------------------
    @staticmethod
    def approval_email(patient_name, claim_id):

        subject = "Healthcare Claim Approved"

        body = f"""
Dear {patient_name},

We are pleased to inform you that your healthcare claim has been APPROVED.

----------------------------------------
Claim Details
----------------------------------------
Claim ID : {claim_id}

Status   : Approved

----------------------------------------

Your claim has been successfully verified and approved.

Thank you for choosing our healthcare insurance services.

Regards,

Healthcare Claims Department
Real-Time Healthcare Claims Analytics Portal
"""

        return subject, body

    # --------------------------------------
    # Rejection Email
    # --------------------------------------
    @staticmethod
    def rejection_email(patient_name, claim_id, reason):

        subject = "Healthcare Claim Rejected"

        body = f"""
Dear {patient_name},

We regret to inform you that your healthcare claim has been REJECTED.

----------------------------------------
Claim Details
----------------------------------------

Claim ID : {claim_id}

Status   : Rejected

Reason   : {reason}

----------------------------------------

If you believe this decision is incorrect, please contact our support team.

Regards,

Healthcare Claims Department
Real-Time Healthcare Claims Analytics Portal
"""

        return subject, body

    # --------------------------------------
    # Status Update Email
    # --------------------------------------
    @staticmethod
    def status_update_email(patient_name, claim_id, status):

        subject = "Healthcare Claim Status Update"

        body = f"""
Dear {patient_name},

Your healthcare claim status has been updated.

----------------------------------------
Claim Details
----------------------------------------

Claim ID : {claim_id}

Current Status : {status}

----------------------------------------

You can log in to the Healthcare Claims Portal to view more details.

Regards,

Healthcare Claims Department
Real-Time Healthcare Claims Analytics Portal
"""

        return subject, body


# ==========================================
# Testing Email Templates
# ==========================================

if __name__ == "__main__":

    print("=" * 60)
    print("APPROVAL EMAIL")
    print("=" * 60)

    subject, body = EmailTemplates.approval_email(
        "Rahul Sharma",
        "C1001"
    )

    print("Subject :", subject)
    print(body)

    print("=" * 60)
    print("REJECTION EMAIL")
    print("=" * 60)

    subject, body = EmailTemplates.rejection_email(
        "Rahul Sharma",
        "C1002",
        "Duplicate Claim Detected"
    )

    print("Subject :", subject)
    print(body)

    print("=" * 60)
    print("STATUS UPDATE EMAIL")
    print("=" * 60)

    subject, body = EmailTemplates.status_update_email(
        "Rahul Sharma",
        "C1003",
        "Pending Verification"
    )

    print("Subject :", subject)
    print(body)