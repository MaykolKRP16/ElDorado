from django.contrib import admin
from VentasApp.models import Cliente,Productos,Categoria
# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombres","apellidos","direccion","telefono")
admin.site.register(Cliente,ClientesAdmin)