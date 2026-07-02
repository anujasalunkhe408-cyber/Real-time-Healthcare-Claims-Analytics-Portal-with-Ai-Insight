import csv
import os

def log_fraud(claim_id, risk_score):

    status = "High Risk"

    file_name = os.path.join(
        "..",
        "reports",
        "fraud_logs.csv"
    )

    with open(file_name, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            claim_id,
            risk_score,
            status
        ])

    print("Fraud activity logged.")