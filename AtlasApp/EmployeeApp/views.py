from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from EmployeeApp.models import Departments,Employees,Vehicles
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer,VehicleSerializer

from django.core.files.storage import default_storage
# Create your views here.

# Departments API Methods
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

#Employees API Methods        

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

# Vehicle API Methods

@csrf_exempt
def vehicleApi(request,id=0):
    if request.method=='GET':
        vehicles = Vehicles.objects.all()
        vehicles_serializer = VehicleSerializer(vehicles, many=True)
        return JsonResponse(vehicles_serializer.data, safe=False)

    elif request.method=='POST':
        vehicle_data=JSONParser().parse(request)
        vehicle_serializer = VehicleSerializer(data=vehicle_data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        vehicle_data = JSONParser().parse(request)
        vehicle=Vehicles.objects.get(VehicleId=vehicle_data['VehicleId'])
        vehicle_serializer=VehicleSerializer(vehicle,data=vehicle_data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        vehicle=Vehicles.objects.get(VehicleId=id)
        vehicle.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

# Save File API Methods
@csrf_exempt
def saveFile(request):
    if request.method=='POST':
        file=request.FILES['file']
        default_storage.save(file.name,file)
        return JsonResponse("File Saved Successfully!!", safe=False)






