from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

def home(request):
    return render(request, 'home.html')

def patients(request):
    data = Patient.objects.all()
    return render(request, 'patients.html', {'data': data})

def about(request):
    return render(request, 'about.html')

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form': form})
def edit_patient(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'edit_patients.html', {'form': form})
def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patients')
from django.db.models import Q

def patients(request):
    query = request.GET.get('q')

    if query:
        data = Patient.objects.filter(
            Q(name__icontains=query) |
            Q(disease__icontains=query)
        )
    else:
        data = Patient.objects.all()

    return render(request, 'patients.html', {
        'data': data
    })