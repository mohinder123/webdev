# Generated by Django 5.0.7 on 2024-07-29 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_watchlist_alter_listing_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='watchlist',
            field=models.BooleanField(default=False),
        ),
    ]
