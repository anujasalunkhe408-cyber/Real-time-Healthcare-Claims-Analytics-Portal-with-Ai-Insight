import pandas as pd
import random
from datetime import datetime, timedelta

# ==========================================
# Sample Data
# ==========================================

diseases = [
    "Diabetes",
    "Cancer",
    "Heart Disease",
    "Asthma",
    "Kidney Stone",
    "Dengue",
    "COVID-19",
    "Fever"
]

genders = [
    "Male",
    "Female"
]

claim_status = [
    "Pending",
    "Approved",
    "Rejected"
]

# ==========================================
# Generate Dataset
# ==========================================

data = []

start_date = datetime(2026, 1, 1)

for i in range(1000):

    claim_id = f"C{1000+i}"

    patient_id = f"P{random.randint(100,999)}"

    patient_name = f"Patient_{random.randint(1,500)}"

    email = f"patient{random.randint(1,500)}@gmail.com"

    age = random.randint(18,80)

    gender = random.choice(genders)

    hospital_id = f"H{random.randint(1,20):03d}"

    disease = random.choice(diseases)

    treatment_cost = random.randint(10000,150000)

    claim_amount = random.randint(8000,180000)

    status = random.choice(claim_status)

    claim_date = (
        start_date +
        timedelta(days=random.randint(0,365))
    ).strftime("%d-%m-%Y")

    # Fraud Rule

    fraud = 1 if claim_amount > treatment_cost * 1.6 else 0

    # Due Date (for reminders)

    due_date = (
        datetime.strptime(claim_date,"%d-%m-%Y")
        + timedelta(days=15)
    ).strftime("%d-%m-%Y")

    data.append([

        claim_id,

        patient_id,

        patient_name,

        email,

        age,

        gender,

        hospital_id,

        disease,

        treatment_cost,

        claim_amount,

        claim_date,

        due_date,

        status,

        fraud

    ])

# ==========================================
# Create DataFrame
# ==========================================

columns = [

    "Claim_ID",

    "Patient_ID",

    "Patient_Name",

    "Email",

    "Age",

    "Gender",

    "Hospital_ID",

    "Disease",

    "Treatment_Cost",

    "Claim_Amount",

    "Claim_Date",

    "Due_Date",

    "Claim_Status",

    "Fraud"

]

df = pd.DataFrame(data, columns=columns)

# ==========================================
# Save CSV
# ==========================================

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")

os.makedirs(DATA_FOLDER, exist_ok=True)

CSV_FILE = os.path.join(DATA_FOLDER, "claims.csv")

df.to_csv(CSV_FILE, index=False)

print("="*60)

print("Healthcare Claims Dataset Generated Successfully")

print("="*60)

print(df.head())

print("\nTotal Records :",len(df))