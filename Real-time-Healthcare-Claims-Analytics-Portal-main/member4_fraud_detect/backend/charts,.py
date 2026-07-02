import pandas as pd
import matplotlib.pyplot as plt
import os

# Get dataset path
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "dataset", "HealthcareClaims.csv")

# Read dataset
df = pd.read_csv(file_path)

# Count fraud and genuine claims
fraud_counts = df["Fraud"].value_counts()

# Create chart
plt.figure(figsize=(6, 5))
fraud_counts.plot(kind="bar")

plt.title("Fraud vs Genuine Claims")
plt.xlabel("Type")
plt.ylabel("Number of Claims")

plt.xticks([0, 1], ["Genuine", "Fraud"])

# Save chart to charts folder
charts_folder = os.path.join(base_dir, "..", "charts")
os.makedirs(charts_folder, exist_ok=True)

chart_path = os.path.join(charts_folder, "fraud_chart.png")

plt.savefig(chart_path)

print("Chart saved at:")
print(chart_path)

plt.show()