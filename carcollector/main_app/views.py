from django.shortcuts import render, redirect
from django.db import models
from .models import Car
from .forms import MaintenanceForm


# Create your views here.

from django.http import HttpResponse

# ##### TEMPORARY ######
# # Add the Cat class & list and view function below the imports
# class Car:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, model, description, year):
#     self.name = name
#     self.model = model
#     self.description = description
#     self.year = year

# cars = [
#   Car('Pilot', 'Honda', 'SUV', 2017),
#   Car('Lexus', 'RX 350', 'Compact SUV', 2020),
#   Car('BMW', '328i', 'Sedan', 2019)
# ]
# ##### TEMPORARY ######

def home(request):
	return HttpResponse('<h1>Car Collector</h1>')

def about(request):
	return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
	car = Car.objects.get(id=car_id)

	maintenance_form = MaintenanceForm()

	return render(request, 'cars/detail.html', {'car': car, 'maintenance_form': maintenance_form})

def add_service(request, car_id):
	form = MaintenanceForm(request.POST)

	if form.is_valid():
		new_service = form.save(commit=False)
		new_service.car_id = car_id
		new_service.save()

	return redirect('detail', car_id=car_id)

