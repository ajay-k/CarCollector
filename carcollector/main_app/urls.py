from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('cars/', views.cars_index, name='index'),
	path('cars/new/', views.new_car, name='new_car'),
	path('cars/<int:car_id>/', views.cars_detail, name='detail'),
	path('cars/<int:car_id>/add_service', views.add_service, name='add_service'),

	path('cars/<int:car_id>/assoc_part/<int:part_id>/', views.assoc_part, name='assoc_part'),

	#CRUD
	path('parts/', views.PartList.as_view(), name='parts_index'),
	path('parts/<int:pk>/', views.PartDetail.as_view(), name='parts_detail'),
	path('parts/create', views.PartCreate.as_view(), name='parts_create'),
	path('parts/<int:pk>/update/', views.PartUpdate.as_view(), name='parts_update'),
	path('parts/<int:pk>/delete/', views.PartDelete.as_view(), name='parts_delete'),
]