# Generated by Django 5.1.7 on 2025-03-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_rename_applicant_income_client_applicantincome_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="name",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="client",
            name="promo_code",
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
