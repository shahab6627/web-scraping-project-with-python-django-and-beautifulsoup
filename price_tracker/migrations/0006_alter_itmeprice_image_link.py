# Generated by Django 4.2.4 on 2023-08-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracker', '0005_alter_itmeprice_item_title_alter_itmeprice_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itmeprice',
            name='image_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]