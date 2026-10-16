
import pandas as pd
import numpy as np
import os

np.random.seed(42)

# Simulated electricity usage ranges (kWh per day)
buildings = {
    "Computer Lab": (80, 180),
    "Library": (40, 100),
    "Classroom": (30, 90),
    "Office": (25, 70),
    "Workshop": (70, 200)
}

data = []

for day in range(1, 31):
    for building, limits in buildings.items():
        electricity = np.random.randint(
            limits[0], limits[1] + 1
        )

        # Occasionally simulate unusually high usage
        if np.random.random() < 0.10:
            electricity = int(electricity * 1.8)

        data.append({
            "Day": day,
            "Building": building,
            "Electricity_kWh": electricity
        })

df = pd.DataFrame(data)

os.makedirs("data", exist_ok=True)
df.to_csv("data/campus_data.csv", index=False)

print("CampusPulse electricity dataset created!")
print(df.head())
print("\nTotal records:", len(df))
print("\nBuildings:", df["Building"].nunique())
