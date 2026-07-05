from django.shortcuts import render, redirect
from .models import Bill
from .forms import BillForm


def bill_list(request):
    bills = Bill.objects.all()
    return render(request, "bill_list.html", {"bills": bills})


def add_bill(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bill_list")
        else:
            print(form.errors)   # ఇది add చేయి
    else:
        form = BillForm()

    return render(request, "add_bill.html", {"form": form})


def delete_bill(request, id):
    bill = Bill.objects.get(id=id)
    bill.delete()
    return redirect("bill_list")