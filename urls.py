from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstpage, name='firstpage'),
    path('units/', views.units, name='units'),
    path('set/<int:pk>/', views.unit_detail, name='unit_detail'),
]