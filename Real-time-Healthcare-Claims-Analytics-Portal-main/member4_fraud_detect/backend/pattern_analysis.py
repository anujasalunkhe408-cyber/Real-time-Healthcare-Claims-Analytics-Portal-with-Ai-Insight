import pandas as pd
import os

# Get the path of the dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "dataset", "HealthcareClaims.csv")

# Read dataset
df = pd.read_csv(file_path)

# Find high claim amounts
high_claims = df[df["Claim_Amount"] > 150000]

print("High Claim Amount Cases:")
print(high_claims[[
    "Claim_ID",
    "Patient_ID",
    "Hospital_ID",
    "Claim_Amount"
]])