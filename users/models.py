from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    session_data = JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class CompanyData(models.Model):
    business = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    tax_reg_no = models.CharField(max_length=50)
    date_of_registration = models.DateTimeField(auto_now=False, auto_now_add=False)
    revenue = models.IntegerField()
    pan = models.CharField(max_length=10)
    misc_data = JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    amount_requested = models.IntegerField()

    Agri = 'Agri'
    Fin = 'Fin'
    Retail = 'Retail'
    Med = 'Med'
    Infra = 'Infra'
    Oth = 'Oth'
    SECTOR_CHOICES = (
        (Agri, settings.SECTORS[0]),
        (Fin, settings.SECTORS[1]),
        (Retail, settings.SECTORS[2]),
        (Med, settings.SECTORS[3]),
        (Infra, settings.SECTORS[4]),
        (Oth, settings.SECTORS[5]))
    sector = models.CharField(max_length=25, choices=SECTOR_CHOICES, default=Oth)

class AnonData(models.Model):
    identifier = models.TextField(unique=True)
    data = JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
