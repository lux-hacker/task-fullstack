from django.contrib.auth.models import User
from django.db import models


class Manager(models.Model):
    name = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Client(models.Model):
    class Status(models.TextChoices):
        IN_WORK = 'В работе', 'In Work'
        OUT_WORK = 'Не в работе', 'Out-Work'
        CLOSE = 'Сделка закрыта', 'Close'
        REJECTED = 'Отказ', 'Rejected'

    account_number = models.CharField(max_length=10)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=8)
    inn = models.IntegerField()
    employer = models.ForeignKey(to=Manager, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=14, choices=Status.choices, default=Status.OUT_WORK)
