# Generated by Django 5.0.7 on 2024-09-18 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerhaApp', '0008_driver_phn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAccepted', models.BooleanField(default=False)),
                ('time', models.TimeField()),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='cerhaApp.driver')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='cerhaApp.student')),
            ],
        ),
    ]
