from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente =models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    direccion = models.CharField(max_length=120)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    estado = models.BooleanField()
    def __str__(self) -> str:
        return self.nombres
    
class Categoria(models.Model):
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()

class Productos(models.Model):
    descripcion=models.CharField(max_length=40)
    categorias=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    precio=models.DecimalField(max_digits = 10,decimal_places = 2)
    cantidad=models.IntegerField()
    estado=models.BooleanField()
