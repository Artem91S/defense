import pandas as pd

from training_of_model import pipeline

new_client = pd.DataFrame(
    {
        "Gender": ["Male"],
        "Married": ["Yes"],
        "Dependents": ["1"],
        "Education": ["Graduate"],
        "Self_Employed": ["No"],
        "ApplicantIncome": [5000],
        "CoapplicantIncome": [2000],
        "LoanAmount": [150],
        "Loan_Amount_Term": [360],
        "Credit_History": [1.0],
        "Property_Area": ["Urban"],
    }
)


prediction = pipeline.predict(new_client)


if prediction[0] == 1:
    print("Кредит схвалено")
else:
    print("Кредит не схвалено")
