# Generated by Django 4.1.5 on 2023-03-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auctionlist_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlist',
            name='seller',
            field=models.CharField(default=True, max_length=64),
        ),
    ]
