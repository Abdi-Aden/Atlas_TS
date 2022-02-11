from rest_framework import serializers
from EmployeeApp.models import Departments, Employees,Vehicles

#department serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')

#vehicle serializer
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('VehicleId',
                  'VehicleName',
                  'VehicleType',
                  'VehicleMake',
                  'VehicleModel',
                  'VehicleColor')

# Employee serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')
                  