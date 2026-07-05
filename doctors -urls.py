from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctors, name='doctors'),
    path('add/', views.add_doctor, name='add_doctor'),
]