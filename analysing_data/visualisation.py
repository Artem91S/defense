import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from clean_data_df import df
from training_of_model import pipeline, categorical_variables, numerical_variables

sns.set(style="whitegrid")
len_numeric = len(numerical_variables)

plt.figure(figsize=(6, 4))
sns.countplot(x=df["Loan_Status"], palette="coolwarm")
plt.title("Розподіл статусу кредиту (Loan_Status)")
plt.xlabel("Loan Status (0 = Відмова, 1 = Схвалено)")
plt.ylabel("Кількість")
plt.show()


plt.figure(figsize=(5 * len_numeric, 5))

for i, col in enumerate(numerical_variables):
    plt.subplot(1, len_numeric, i + 1)
    sns.histplot(df[col], bins=30, kde=True, color="blue")
    plt.title(f"Розподіл {col}")

plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x="Credit_History", hue="Loan_Status", data=df, palette="coolwarm")
plt.title("Кредитна історія та схвалення кредиту")
plt.xlabel("Credit History (0 = Немає, 1 = Є)")
plt.ylabel("Кількість заявок")
plt.legend(["Не схвалено", "Схвалено"])
plt.show()


plt.figure(figsize=(15, 10))
for i, col in enumerate(categorical_variables):
    plt.subplot(2, 3, i + 1)
    sns.countplot(x=col, hue="Loan_Status", data=df, palette="coolwarm")
    plt.title(f"{col} та статус кредиту")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Кореляційна матриця")
plt.show()

importances = pipeline.named_steps["classifier"].feature_importances_
feature_names = (
    numerical_variables
    + list(pipeline.named_steps["preprocessor"].transformers_[1][1].get_feature_names_out(categorical_variables))
)



plt.figure(figsize=(12, 6))
indices = np.argsort(importances)[::-1]
plt.bar(range(len(importances)), importances[indices], align="center")
plt.xticks(range(len(importances)), np.array(feature_names)[indices], rotation=90)
plt.title("Важливість ознак у моделі RandomForest")
plt.show()
