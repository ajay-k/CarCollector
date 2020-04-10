from django.contrib import admin

# Register your models here.
from .models import Car, Maintenance, Part

admin.site.register(Car)
admin.site.register(Maintenance)
admin.site.register(Part)