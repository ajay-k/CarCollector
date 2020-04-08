from django.db import models

# Create your models here.
SERVICES = (
		('O', 'Oil Change'),
		('T', 'Tire Rotation'),
		('B', 'Battery Replacement')
	)

class Car(models.Model):
	make = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	trim = models.CharField(max_length=100)
	year = models.IntegerField()

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
