# Generated by Django 5.0.7 on 2024-11-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerhaApp', '0022_usersecurityanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
