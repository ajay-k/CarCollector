from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.
SERVICES = (
		('O', 'Oil Change'),
		('T', 'Tire Rotation'),
		('B', 'Battery Replacement')
	)

class Part(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('parts_detail', kwargs={"pk": self.id})

class Car(models.Model):
	make = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	trim = models.CharField(max_length=100)
	year = models.IntegerField()

	#Adds Many-to-Many relationship
	parts = models.ManyToManyField(Part)

	def __str__(self):
		return self.make


class Maintenance(models.Model):
	date = models.DateField('Service Date')
	service = models.CharField(
		max_length=1,
		choices=SERVICES,
		default=SERVICES[0][0]
	)

	car = models.ForeignKey(Car, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.get_service_display()} on {self.date}"

	class Meta:
		ordering = ['-date']
