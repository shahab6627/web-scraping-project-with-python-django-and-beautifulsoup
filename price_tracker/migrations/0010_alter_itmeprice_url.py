# Generated by Django 4.2.4 on 2023-08-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracker', '0009_alter_itmeprice_current_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itmeprice',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
