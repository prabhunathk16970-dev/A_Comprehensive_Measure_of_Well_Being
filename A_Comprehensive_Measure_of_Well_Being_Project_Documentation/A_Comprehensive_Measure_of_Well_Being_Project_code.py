import pandas as pd
import numpy as np

# Reproducible random data
np.random.seed(42)

rows = 1000

# Features
age = np.random.randint(18, 60, rows)
gender = np.random.choice(["Male", "Female"], rows)
sleep = np.random.uniform(4, 10, rows).round(1)
exercise = np.random.randint(0, 7, rows)
water = np.random.uniform(1, 4, rows).round(1)
screen = np.random.uniform(1, 10, rows).round(1)
stress = np.random.randint(1, 11, rows)
diet = np.random.randint(1, 11, rows)
work = np.random.uniform(4, 12, rows).round(1)
social = np.random.uniform(0, 5, rows).round(1)

# Well-Being Score (Synthetic Formula)
wellbeing = (
    sleep * 8
    + exercise * 4
    + water * 5
    - screen * 2
    - stress * 3
    + diet * 3
    - work * 1.5
    + social * 4
    + np.random.normal(0, 3, rows)
)

# Limit score to 0–100
wellbeing = np.clip(wellbeing, 0, 100).round(2)

# Create DataFrame
df = pd.DataFrame({
    "Age": age,
    "Gender": gender,
    "Sleep_Hours": sleep,
    "Exercise_Days": exercise,
    "Water_Intake_Liters": water,
    "Screen_Time_Hours": screen,
    "Stress_Level": stress,
    "Diet_Quality": diet,
    "Work_Hours": work,
    "Social_Time": social,
    "WellBeing_Score": wellbeing
})

# Save CSV
df.to_csv("wellbeing_dataset.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
print(f"\nTotal records: {len(df)}")