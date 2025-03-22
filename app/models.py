from django.db import models


# print(set(df['Gender'])) # {'Female', 'Male'}
# print(set(df['Married'])) # {'No', 'Yes'}
# print(set(df['Education'])) # {'Not Graduate', 'Graduate'}
# print(set(df['Self_Employed'])) # {'No', 'Yes'}
# print(set(df['Property_Area'])) # {'Semiurban', 'Urban', 'Rural'}


class Client(models.Model):
    class Gender(models.TextChoices):
        FEMALE = 'Female'
        MALE = 'Male'

    class MarriedAndEmployed(models.TextChoices):
        YES = 'Yes'
        NO = 'No'

    class Education(models.TextChoices):
        NOT_GRADUATE = 'Not Graduate'
        GRADUATE = 'Graduate'

    class PropertyArea(models.TextChoices):
        SEMIURBAN = 'Semiurban'
        URBAN = 'Urban'
        RURAL = 'Rural'

    class Dependents(models.TextChoices):
        ZERO = '0'
        FIRST = '1'
        TWO = '2'
        THREE_OR_MORE = '3+'

    class HISTORY(models.IntegerChoices):
        NO = 0.0
        YES = 1.0

    Gender = models.CharField(max_length=6, choices=Gender, default=Gender.MALE)
    Married = models.CharField(max_length=3,choices=MarriedAndEmployed, default=MarriedAndEmployed.YES)
    Dependents = models.CharField(max_length=2, choices=Dependents, default=Dependents.ZERO)
    Education = models.CharField(max_length=12,choices=Education, default=Education.GRADUATE)
    Self_Employed = models.CharField(max_length=3, choices=MarriedAndEmployed, default=MarriedAndEmployed.NO)
    ApplicantIncome = models.IntegerField(null=False)
    CoapplicantIncome = models.FloatField(null=False)
    LoanAmount = models.FloatField(null=False)
    Loan_Amount_Term = models.FloatField(null=False)
    Credit_History = models.FloatField(choices=HISTORY, default=HISTORY.NO, null=False)
    Property_Area = models.CharField(max_length=9,choices=PropertyArea, default=PropertyArea.URBAN)
    name = models.CharField(max_length=20,blank=True, null=False)
    promo_code = models.UUIDField(blank=True, null=True)

    def __str__(self):
        return f'Gender:-> {self.get_Gender_display()},Married:->{self.get_Married_display()}'
