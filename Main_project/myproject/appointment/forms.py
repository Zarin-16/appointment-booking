from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

# class DateForm(forms.Form):
#     appointment_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

