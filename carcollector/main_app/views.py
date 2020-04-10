from django.shortcuts import render, redirect
from django.db import models
from .models import Car, Part
from .forms import CarForm, MaintenanceForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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

	parts_car_doesnt_have = Part.objects.exclude(id__in = car.parts.all().values_list('id'))

	maintenance_form = MaintenanceForm()

	return render(request, 'cars/detail.html', {'car': car, 'maintenance_form': maintenance_form, 'parts': parts_car_doesnt_have})

def add_service(request, car_id):
	form = MaintenanceForm(request.POST)

	if form.is_valid():
		new_service = form.save(commit=False)
		new_service.car_id = car_id
		new_service.save()

	return redirect('detail', car_id=car_id)

def assoc_part(request, car_id, part_id):
	Car.objects.get(id=car_id).parts.add(part_id)

	return redirect('detail', car_id=car_id)

def new_car(request):
	if(request.method == 'POST'):

		form = CarForm(request.POST)
		if form.is_valid():
			car =  form.save()

			return redirect('detail', car.id)
	else:
		form = CarForm()

	context = { 'form': form}

	return render(request, 'cars/car_form.html', context)



#------------------------------------
# Class-based Views for the Toy model
#------------------------------------
# CBVs are great for getting basic CRUD functionality 
# up and running in a very short period of time. However,
# CBVs are not a coding pattern that you are likely to see
# in production Django apps. We used them here to free up 
# time for lessons. Read the documentation below to get a
# brief introduction CBVs.

# CBVs fall into 5 types: List, Detail, Create, Update, Delete
# Notice that each class below inherits from one of those 5 types

# List and Detail Views are the easiest to set up; all we need to 
# do is declare the model we want to build a view for.
class PartList(ListView):
  # This line associates the ListView with the Toy model
  model = Part

class PartDetail(DetailView):
  model = Part

# The editable view types include Create, Update, and Delete
# They're also relatively easy to set up but require a little more work
class PartCreate(CreateView):
  model = Part
  # The CreateView requires a field property to set
  # Here we are saying that all fields associated with a Toy should 
  # be displayed in the form
  fields = '__all__'
  # This CBV will render the template toy_form.html  

class PartUpdate(UpdateView):
  model = Part
  # In the UpdateView we set the name and color fields as the only two in the form
  fields = ['name', 'color']
  # This CBV will render the template toy_form.html as well


class PartDelete(DeleteView):
  model = Part
  # The DeleteView requires a success_url be declared to redirect 
  # the user to when they successfully delete a toy
  success_url = '/parts/'
  # This CBV will render the toy_confirm_delete.html template 
