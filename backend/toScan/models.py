from django.conf import settings
from django.db import models


class ListToValidate(models.Model):
    "Generated Model"
    idBox = models.CharField(max_length=30,)
    estado = models.BigIntegerField(null=True, blank=True,)
    numeroCaja = models.CharField(max_length=256, null=True, blank=True,)
    pallet = models.CharField(max_length=12, null=True, blank=True,)
    idCliente = models.TextField(null=True, blank=True,)


# Create your models here.
