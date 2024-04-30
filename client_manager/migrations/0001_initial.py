# Generated by Django 5.0.4 on 2024-04-16 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('inn', models.IntegerField()),
                ('employer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_manager.user')),
            ],
        ),
    ]