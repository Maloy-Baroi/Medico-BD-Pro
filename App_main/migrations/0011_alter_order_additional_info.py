# Generated by Django 4.0.6 on 2022-07-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0010_order_additional_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='additional_info',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
