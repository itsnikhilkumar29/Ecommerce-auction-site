# Generated by Django 3.0.5 on 2021-02-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]