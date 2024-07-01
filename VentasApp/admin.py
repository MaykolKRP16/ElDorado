from django.contrib import admin
from VentasApp.models import Cliente, Ruta, Carro, Reserva, Boleto, Asiento
from VentasApp.forms import BoletoForm

class BoletoAdmin(admin.ModelAdmin):
    form = BoletoForm

admin.site.register(Cliente)
admin.site.register(Ruta)
admin.site.register(Carro)
admin.site.register(Reserva)
admin.site.register(Boleto, BoletoAdmin)
admin.site.register(Asiento)