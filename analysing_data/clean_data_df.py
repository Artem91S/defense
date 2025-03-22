import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(current_dir, "loan_data.csv")

df = pd.read_csv(csv_path)

df = df.copy()

df.loc[:, "Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Dependents"] = df["Dependents"].fillna("0")
df["Self_Employed"] = df["Self_Employed"].fillna("No")
df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())
df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

df["Self_Employed"] = df["Self_Employed"].astype(str)
df["Gender"] = df["Gender"].astype(str)
df["Married"] = df["Married"].astype(str)
df["Education"] = df["Education"].astype(str)
df["Property_Area"] = df["Property_Area"].astype(str)

statistics = df.describe()

correlation = df.corr(numeric_only=True)

missing_values = df.isna().sum()

# print(set(df['Gender']))
# print(set(df['Married']))
# print(set(df['Education']))
# print(set(df['Self_Employed']))
# print(set(df['Property_Area']))
# print(set(df['Dependents']))