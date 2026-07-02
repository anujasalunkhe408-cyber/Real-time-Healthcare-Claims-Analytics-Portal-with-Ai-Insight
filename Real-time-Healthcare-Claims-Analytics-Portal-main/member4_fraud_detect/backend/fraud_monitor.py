from notify_admin import notify_admin
from log_activity import log_fraud

claim_id = "C1001"
risk_score = 89

if risk_score >= 70:

    notify_admin(claim_id, risk_score)

    log_fraud(claim_id, risk_score)

    print("Alert generated successfully.")