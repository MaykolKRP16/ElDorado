from django import forms
from VentasApp.models import Boleto, Asiento, Reserva

class BoletoForm(forms.ModelForm):
    class Meta:
        model = Boleto
        fields = ['reserva', 'numero_asiento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'reserva' in self.data:
            try:
                reserva_id = int(self.data.get('reserva'))
                reserva = Reserva.objects.get(idReserva=reserva_id)  # Cambiado de 'id' a 'idReserva'
                self.fields['numero_asiento'].queryset = Asiento.objects.filter(carro_id=reserva.carro_id, disponible=True)
            except (ValueError, TypeError, Reserva.DoesNotExist):
                self.fields['numero_asiento'].queryset = Asiento.objects.none()
        elif self.instance.pk:
            self.fields['numero_asiento'].queryset = Asiento.objects.filter(carro_id=self.instance.reserva.carro_id, disponible=True)