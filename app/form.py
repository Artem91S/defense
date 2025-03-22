from django import forms
from .models import Client


class CreditForm(forms.ModelForm):
    # gender = forms.ChoiceField(choices=Client.Gender.choices, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Client
        fields = ['name', 'Gender', 'Married', 'Dependents',
                  'Education', 'Self_Employed', 'ApplicantIncome',
                  'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
                  'Credit_History', 'Property_Area'
                  ]
        labels = {
            'name': 'Name:',
            'Gender': 'Gender:',
            'Married': 'Married:',
            'Dependents': 'Dependents:',
            'Education': 'Education:',
            'Self_Employed': 'Self Employed:',
            'ApplicantIncome': 'Applicant Income:',
            'CoapplicantIncome': 'Co Applicant Income:',
            'LoanAmount': 'Loan Amount:',
            'Loan_Amount_Term': 'Loan Amount Term:',
            'Credit_History': 'Credit History:',
            'Property_Area': 'Property Area:'
        }

    def clean_ApplicantIncome(self):
        ApplicantIncome = int(self.cleaned_data['ApplicantIncome'])
        if ApplicantIncome <= 0:
            raise forms.ValidationError('ApplicantIncome can not be below 0 or equal 0')
        return ApplicantIncome

    def clean_CoapplicantIncome(self):
        CoapplicantIncome = int(self.cleaned_data['CoapplicantIncome'])
        if CoapplicantIncome <= 0:
            raise forms.ValidationError('CoapplicantIncome can not be below 0 or equal 0')
        return CoapplicantIncome

    def clean_LoanAmount(self):
        LoanAmount = int(self.cleaned_data['LoanAmount'])
        if LoanAmount <= 0:
            raise forms.ValidationError('LoanAmount can not be below 0 or equal 0')
        return LoanAmount

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3 or len(name) > 20:
            raise forms.ValidationError('The name can be more than 3 letters and less than 20.')
        return name
