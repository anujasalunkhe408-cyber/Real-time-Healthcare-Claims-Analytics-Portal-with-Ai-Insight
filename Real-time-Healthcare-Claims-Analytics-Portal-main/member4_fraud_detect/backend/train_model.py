import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "dataset", "HealthcareClaims.csv")

df = pd.read_csv(file_path)

print("Dataset Loaded Successfully!")
print(df.head())

# Convert text columns into numbers
label_encoder = LabelEncoder()

text_columns = [
    "Gender",
    "Hospital_ID",
    "Disease",
    "Claim_Status"
]

for col in text_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Features (Input)
X = df.drop(["Claim_ID", "Patient_ID", "Fraud", "Claim_Date"], axis=1)

# Target (Output)
y = df["Fraud"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model
model_dir = os.path.join(base_dir, "..", "model")
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, "fraud_model.pkl")

joblib.dump(model, model_path)

print("\nModel saved at:")
print(model_path)
print("\nModel Saved Successfully!")