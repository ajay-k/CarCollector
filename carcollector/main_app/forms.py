from django.forms import ModelForm
from .models import Car,Maintenance
from django import forms

class CarForm(forms.ModelForm):

	class Meta:
		model = Car
		fields = {'model', 'make', 'trim', 'year'}

class MaintenanceForm(ModelForm):
	class Meta:
		model = Maintenance
		fields = ['date', 'service']