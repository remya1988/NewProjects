# Generated by Django 4.0.6 on 2022-07-26 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='p_name',
        ),
    ]
