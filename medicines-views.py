from django.shortcuts import render, redirect
from .models import Medicine
from .forms import MedicineForm

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, "medicine_list.html", {"medicines": medicines})

def add_medicine(request):
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("medicine_list")
    else:
        form = MedicineForm()

    return render(request, "add_medicine.html", {"form": form})