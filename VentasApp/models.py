from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    direccion = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Ruta(models.Model):
    idRuta = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia_km = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.origen} - {self.destino}"

class Carro(models.Model):
    idCarro = models.AutoField(primary_key=True)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    fecha_salida = models.DateTimeField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    es_doble_piso = models.BooleanField(default=False)

    def __str__(self):
        return f"Carro {self.idCarro} - {self.ruta.origen} a {self.ruta.destino}"

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, default=1)  # Suponiendo que el ID 1 es un carro válido
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad_boletos = models.PositiveIntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva {self.idReserva} - Cliente: {self.cliente}, Carro: {self.carro}"

class Asiento(models.Model):
    idAsiento = models.AutoField(primary_key=True)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    numero_asiento = models.CharField(max_length=10)
    piso = models.CharField(max_length=1, blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Asiento {self.numero_asiento} en Carro {self.carro.idCarro}"

class Boleto(models.Model):
    idBoleto = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    numero_asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE)

    @property
    def costo(self):
        return self.reserva.carro.precio_base

    def __str__(self):
        return f"Boleto {self.idBoleto} - Reserva: {self.reserva}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.numero_asiento.disponible = False
        self.numero_asiento.save()
    
@receiver(post_save, sender=Carro)
def crear_asientos(sender, instance, created, **kwargs):
    if created:
        if instance.es_doble_piso:
            for piso in ['A', 'B']:
                for i in range(1, 31):
                    Asiento.objects.create(carro=instance, numero_asiento=f"{piso}{i:02d}", piso=piso)
        else:
            for i in range(1, 31):
                Asiento.objects.create(carro=instance, numero_asiento=f"{i:02d}")