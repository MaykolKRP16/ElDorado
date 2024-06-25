from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente =models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80)
