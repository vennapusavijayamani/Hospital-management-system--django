from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Bill(models.Model):
    PAYMENT_STATUS = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]

    PAYMENT_METHOD = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Card', 'Card'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    appointment_date = models.DateField()

    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    medicine_fee = models.DecimalField(max_digits=10, decimal_places=2)
    lab_fee = models.DecimalField(max_digits=10, decimal_places=2)
    other_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)

    payment_date = models.DateField()

    def save(self, *args, **kwargs):
        self.total_amount = (
            self.consultation_fee +
            self.medicine_fee +
            self.lab_fee +
            self.other_fee -
            self.discount
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.id} - {self.patient.name}"