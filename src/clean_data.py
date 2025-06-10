import pandas as pd

df = pd.read_csv("data/diabetes.csv")

#replace 0 in glucose with median
glucose_median = df['Glucose'].median()
df['Glucose'] = df['Glucose'].replace(0, glucose_median)

#replace 0 in bloodpressure with median
bp_median = df['BloodPressure'].median()
df['BloodPressure'] = df['BloodPressure'].replace(0, bp_median)

# save cleaned data
df.to_csv("data/diabetes_cleaned.csv", index=False)