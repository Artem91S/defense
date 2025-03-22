# Loan Prediction Web Application

### 📌 Description of project: 
This Django web application uses a machine learning model to predict the probability of loan approval based on user-entered data.

### 📂Folder analysing_data:
- **clean_data_df.py** – file where we prepare data.
- **loan_data.csv** – input dataset for training the model.
- **example_work.py** – example of model work.
- **training_of_model.py** – example of model work.
- **visualisation.py** – visualisation of main data info by matplotlib and seaborn.
### 📂Folder create_broker and app
- **create_broker/** – main Django app with all settings.
- **app/** – app with template, views, forms, models.
- **static/** – images and styles.

### 🚀 How to start:
1. Create venv:
    ```bash
   python -m venv venv  
   
2. Activate venv:
   #### For MacOS:
   ```bash
   source venv/bin/activate
   ```
   #### For Windows:
   ```bash
   source venv/Scripts/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Perform migrations:
    ```bash
    python manage.py migrate
    
5. Start the server:
    ```bash
    python manage.py runserver
   

## 🎯Functionality
- **Form for entering loan parameters;**
- **Prediction of the result based on the trained model;**
- **Display of the result (approved / not approved).**


## 📝 Technical details
- **Backend: Django, Django Forms;**
- **ML model: Pipeline (with sklearn.pipeline.Pipeline);**
- **Feature processing: ColumnTransformer;**
- **Categorical encoding: OneHotEncoder;**
- **Numeric scaling: StandardScaler;**
- **Classifier: RandomForestClassifier;**
- **Model scoring: GridSearchCV;**
- **Data splitting: train_test_split;**
- **Frontend: HTML, CSS;**
- **Database: SQLite.**


## 📖 Using
- **Enter the parameters in the form;**
- **Get instant results;**
- **If the loan is not approved, try changing the terms.**

## After start app go to website 

[Go to website](http://127.0.0.1:8000/credit)