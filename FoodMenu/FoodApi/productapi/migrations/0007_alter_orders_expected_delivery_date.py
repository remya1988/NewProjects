# Generated by Django 4.0.6 on 2022-08-17 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0006_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.date(2022, 8, 22), null=True),
        ),
    ]