from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('cars/', views.cars_index, name='index'),
	path('cars/<int:car_id>/', views.cars_detail, name='detail'),
	path('cars/<int:car_id>/add_service', views.add_service, name='add_service'),
]