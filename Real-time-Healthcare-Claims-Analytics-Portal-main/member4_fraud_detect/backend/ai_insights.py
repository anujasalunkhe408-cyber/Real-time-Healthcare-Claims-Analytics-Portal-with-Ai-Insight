import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "dataset", "HealthcareClaims.csv")

df = pd.read_csv(file_path)

# Top hospital by number of claims
top_hospital = df["Hospital_ID"].value_counts().idxmax()
hospital_count = df["Hospital_ID"].value_counts().max()

# Patient with most claims
top_patient = df["Patient_ID"].value_counts().idxmax()
patient_count = df["Patient_ID"].value_counts().max()

print("===== AI INSIGHTS =====")
print(f"Hospital {top_hospital} submitted {hospital_count} claims.")
print(f"Patient {top_patient} submitted {patient_count} claims.")