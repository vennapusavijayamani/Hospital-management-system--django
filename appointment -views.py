from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm


def appointments(request):
    data = Appointment.objects.all()
    return render(request, "appointment.html", {"appointments": data})


def add_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("appointments")
    else:
        form = AppointmentForm()

    return render(request, "book_appointment.html", {"form": form})


def delete_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect("appointments")
from django.shortcuts import get_object_or_404

def edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect("appointments")
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, "book_appointment.html", {"form": form})