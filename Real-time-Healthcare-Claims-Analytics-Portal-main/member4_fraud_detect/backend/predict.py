import pandas as pd
import joblib
import os

# Load model
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "..", "model", "fraud_model.pkl")

model = joblib.load(model_path)

# New claim data
new_claim = {
    "Age": 45,
    "Gender": 1,          # Male=1, Female=0 (may vary)
    "Hospital_ID": 5,
    "Disease": 2,
    "Treatment_Cost": 30000,
    "Claim_Amount": 150000,
    "Claim_Status": 1
}

df = pd.DataFrame([new_claim])

prediction = model.predict(df)
probability = model.predict_proba(df)

risk_score = probability[0][1] * 100

print("Fraud Prediction:", prediction[0])
print("Risk Score:", round(risk_score, 2), "%")