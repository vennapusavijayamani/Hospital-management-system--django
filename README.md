
Hospital Management System - Project Steps

Step 1: Create the Django Project
First, I created a Django project named Hospital Management System (HMS).

django-admin startproject hms

Step 2: Create Applications (Apps)
I created separate apps for each module:
Patients
Doctors
Appointments
Billing
Medicines

python manage.py startapp patients
python manage.py startapp doctors
python manage.py startapp appointments
python manage.py startapp billing
python manage.py startapp medicines

Step 3: Register Apps
I added all the apps in the INSTALLED_APPS section of settings.py.

Step 4: Create Models
I created database models for:
Patient
Doctor
Appointment
Bill
Medicine
These models automatically create database tables.

Step 5: Apply Migrations
After creating models, I generated and applied migrations.

python manage.py makemigrations
python manage.py migrate

Step 6: Create Superuser
I created a Django Admin account.

python manage.py createsuperuser

Step 7: Register Models in Admin
I registered all models in admin.py so they appear in the Django Admin Panel.

Step 8: Create Forms
I created ModelForms to collect user input.
Example:
Patient Form
Doctor Form
Bill Form

Step 9: Create Views
I created views to perform CRUD operations:
Add
View
Update
Delete

Step 10: Configure URLs
I connected all pages using Django URL routing.
Example:
/patients/
/doctors/
/appointments/
/billing/
/medicines

Step 11: Create Templates
I designed HTML pages using:
HTML
CSS
Bootstrap
Pages include:
Home Page
Patient List
Doctor List
Appointment List
Billing List
Medicine List

Step 12: Run the Project
Finally, I started the Django development server.

python manage.py runserver

Then I opened:
http://127.0.0.1:8000/
Redirect in Django
After saving or deleting data, I redirected the user to another page.
Example:
return redirect('patient_list')
Why is Redirect used?
To automatically move the user to another page after an action.
To improve user experience.
To prevent duplicate form submission.
Technologies Used
Python
Django
HTML
CSS
Bootstrap
SQLite3
Modules
Admin Login
Patient Management
Doctor Management
Appointment Management
Billing Management
Medicine Management
Project Outcome
The Hospital Management System helps hospitals manage patient records, doctor details, appointments, billing, and medicines digitally. It reduces paperwork, saves time, and improves data management.

This version is suitable for PPT, Project Report, and Viva because it is simple, professional, and easy to explain.# Hospital-management-system--django