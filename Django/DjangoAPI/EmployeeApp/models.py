from django.db import models

# Create your models here.
#department model
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

#vehicle model
class Vehicles(models.Model):
    VehicleId = models.AutoField(primary_key=True)
    VehicleName = models.CharField(max_length=100)
    VehicleType = models.CharField(max_length=100)
    VehicleMake = models.CharField(max_length=100)
    VehicleModel = models.CharField(max_length=100)
    VehicleColor = models.CharField(max_length=100)

# Employee model
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    EmployeeVehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    PhotoFileName = models.CharField(max_length=100)
