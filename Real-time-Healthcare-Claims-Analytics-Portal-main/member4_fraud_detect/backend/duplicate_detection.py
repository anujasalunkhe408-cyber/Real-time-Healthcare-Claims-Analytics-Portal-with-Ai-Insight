import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "dataset", "HealthcareClaims.csv")

df = pd.read_csv(file_path)

duplicates = df[df.duplicated(
    subset=["Patient_ID", "Claim_Amount", "Claim_Date"],
    keep=False
)]

print(duplicates)