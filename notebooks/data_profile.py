import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data/diabetes.csv") # Load data as dataframe
# detailed analysis-basic statistics(mean, median etc.),
# Data Types, Missing values, Correlations, data quality issues etc.
profile = ProfileReport(df, title="Data Profile") 
profile.to_file("reports/data_profile.html") # Save report as HTML file
