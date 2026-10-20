import os
import pandas as pd

# Create data folder
os.makedirs("data", exist_ok=True)

# Create sample dataset
df = pd.DataFrame({
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Age": [22, 24, 21, 23, 25],
    "City": ["Delhi", "Gurgaon", "Patna", "Mumbai", "Noida"],
    "Salary": [25000, 30000, 22000, 35000, 40000]
})

# Save CSV file
df.to_csv("data/sample_data.csv", index=False)

print("CSV file created successfully!")
print(df)