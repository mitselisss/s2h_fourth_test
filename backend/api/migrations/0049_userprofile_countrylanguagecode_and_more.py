# Generated by Django 4.2.2 on 2023-07-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='countryLanguageCode',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='userprofilehistory',
            name='countryLanguageCode',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
