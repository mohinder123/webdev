# Generated by Django 5.0.7 on 2024-10-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerhaApp', '0009_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(default='NULL', max_length=128),
        ),
        migrations.AlterField(
            model_name='driver',
            name='phn',
            field=models.IntegerField(max_length=10, unique=True),
        ),
    ]
