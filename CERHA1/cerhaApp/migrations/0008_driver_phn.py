# Generated by Django 5.0.7 on 2024-09-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerhaApp', '0007_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='phn',
            field=models.IntegerField(default=0, max_length=10, unique=True),
        ),
    ]
