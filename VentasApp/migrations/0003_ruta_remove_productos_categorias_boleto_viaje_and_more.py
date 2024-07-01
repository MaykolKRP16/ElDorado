# Generated by Django 5.0.6 on 2024-07-01 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VentasApp', '0002_categoria_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('idRuta', models.AutoField(primary_key=True, serialize=False)),
                ('origen', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('distancia_km', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='productos',
            name='categorias',
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('idBoleto', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentasApp.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('idViaje', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_salida', models.DateTimeField()),
                ('capacidad_maxima', models.PositiveIntegerField()),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentasApp.ruta')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idReserva', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_boletos', models.PositiveIntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentasApp.cliente')),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentasApp.viaje')),
            ],
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
    ]
