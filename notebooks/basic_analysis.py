import pandas as pd
df = pd.read_csv("data/diabetes.csv")

# show first 5 rows
print("First 5 rows")
print(df.head())

# summary statistics
print("basic statistics")
print(df.describe())

# missing values
print("Missing values")
print(df.isnull().sum())

#correlation matrix
print("Correlation matrix")
print(df.corr())

# Rule based validation examples
print("Checking for invalid values")

# blood pressure cannot be 0
invalid_bp = df[ df["BloodPressure"] == 0]
print("Invalid blood pressure count: ", len(invalid_bp))

# glucose cannot be 0
invalid_glucose = df[ df['Glucose'] == 0]
print(f"Invalid Glucose entries: {len(invalid_glucose)}")
