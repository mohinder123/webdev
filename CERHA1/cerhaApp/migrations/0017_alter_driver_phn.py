# Generated by Django 5.0.7 on 2024-10-21 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerhaApp', '0016_alter_driver_vehicleno_alter_student_rollno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phn',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must be exactly 10 digits.', regex='^\\d{10}$')]),
        ),
    ]
