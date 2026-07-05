from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm

def doctors(request):
    data = Doctor.objects.all()
    return render(request, 'doctors.html', {'data': data})

def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()

    return render(request, 'add_doctor.html', {'form': form})