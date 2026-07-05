from django.urls import path
from . import views

urlpatterns = [
    path("", views.appointments, name="appointments"),
    path("book/", views.add_appointment, name="book_appointment"),
    path("delete/<int:id>/", views.delete_appointment, name="delete_appointment"),
    path("edit/<int:id>/", views.edit_appointment, name="edit_appointment"),
]