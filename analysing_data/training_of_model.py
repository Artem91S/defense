from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score

from analysing_data.clean_data_df import df

categorical_variables = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
]
numerical_variables = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History",
]

X = df.drop(columns=["Loan_ID", "Loan_Status"])
y = df["Loan_Status"].map({"Y": 1, "N": 0})

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_variables),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_variables),
    ]
)

pipeline = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(random_state=42)),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline.fit(X_train, y_train)

result = pipeline.score(X_test, y_test)

print(f"Точність моделі: {round(result,2)}")

params = {
    "classifier__n_estimators": [50, 100, 200],
    "classifier__max_depth": [None, 10, 20],
    "classifier__min_samples_split": [2, 5, 10],
}

search = GridSearchCV(pipeline, params, cv=5, scoring="accuracy", n_jobs=-1)
search.fit(X_train, y_train)
