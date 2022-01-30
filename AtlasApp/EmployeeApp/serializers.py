
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees, Vehicles

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('VehicleId',
                  'VehicleName',
                  'VehicleMake',
                  'VehicleModel',
                  'VehiclePlate'
                  'VehicleYear',
                  'PhotoFileName')                  