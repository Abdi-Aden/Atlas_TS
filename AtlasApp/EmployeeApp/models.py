
import email
from lib2to3.pgen2 import driver
from django.db import models
import uuid 




# Create your models here.

class Departments(models.Model):
    department_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_name = models.CharField(max_length=100)
    department_manager = models.CharField(max_length=100)
    department_location = models.CharField(max_length=100)
    department_phone = models.CharField(max_length=100)
    department_email = models.EmailField(max_length=100)


class Vehicles(models.Model):
    vehicle_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_year = models.CharField(max_length=100)
    vehicle_color = models.CharField(max_length=100)
    vehicle_license = models.CharField(max_length=100)
    vehicle_vin = models.CharField(max_length=100)
    vehicle_license_plate = models.CharField(max_length=100)
    vehicle_documents = models.FileField(upload_to='documents/')
    


class Employees(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_first_name = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=100)
    employee_dob = models.DateField()
    employee_ssn = models.CharField(max_length=100)
    employee_address = models.CharField(max_length=100)
    employee_email = models.EmailField(max_length=100)
    employee_phone = models.CharField(max_length=100)
    employee_hire_date = models.DateField()
    employee_position = models.CharField(max_length=100)
    employee_department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    employee_vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    employee_license = models.CharField(max_length=100)
    employee_license_state = models.CharField(max_length=100)
    employee_license_number = models.CharField(max_length=100)
    employee_license_expiration = models.DateField()
    employe_documents = models.FileField(upload_to='documents/')