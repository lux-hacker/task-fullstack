# Generated by Django 5.0.4 on 2024-04-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_manager', '0003_client_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birth_date',
            field=models.CharField(max_length=8),
        ),
    ]