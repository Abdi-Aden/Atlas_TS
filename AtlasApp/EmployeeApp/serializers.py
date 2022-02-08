
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees, Vehicles


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('department_id', 'department_name', 'department_manager', 'department_location', 'department_phone', 'department_email')


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employee_id', 'employee_first_name', 'employee_last_name', 'employee_dob', 'employee_ssn', 'employee_address', 'employee_email', 'employee_phone', 'employee_hire_date', 'employee_position', 'employee_department', 'employee_vehicle', 'employee_license', 'employee_license_state', 'employee_license_number', 'employee_license_expiration', 'employe_documents') 


class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('vehicle_id', 'vehicle_name', 'vehicle_type', 'vehicle_make', 'vehicle_model', 'vehicle_year', 'vehicle_color', 'vehicle_license', 'vehicle_vin', 'vehicle_license_plate', 'vehicle_documents')


