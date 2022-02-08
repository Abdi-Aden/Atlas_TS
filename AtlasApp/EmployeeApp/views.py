
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import HttpResponse
from django.http.response import JsonResponse


from EmployeeApp.models import Departments, Employees, Vehicles
from EmployeeApp.serializers import DepartmentsSerializer, EmployeesSerializer, VehiclesSerializer


# Create your views here.

# Departments API
@csrf_exempt
def departmentApi(request,id=0):
    if request.method == 'GET':
        if id == 0:
            departments = Departments.objects.all()
            serializer = DepartmentsSerializer(departments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            departments = Departments.objects.get(department_id=id)
            serializer = DepartmentsSerializer(departments, many=False)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse( request )
        serializer = DepartmentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        data = JSONParser().parse( request )
        department = Departments.objects.get(department_id=id)
        serializer = DepartmentsSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        department = Departments.objects.get(department_id=id)
        department.delete()
        return HttpResponse(status=204)


# Employees API
@csrf_exempt
def employeeApi(request,id=0):
    if request.method == 'GET':
        if id == 0:
            employees = Employees.objects.all()
            employees_serializer = EmployeesSerializer(employees, many=True)
            return JsonResponse(employees_serializer.data, safe=False)
        else:
            employees = Employees.objects.get(employee_id=id)
            employees_serializer = EmployeesSerializer(employees, many=False)
            return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data=JSONParser().parse(request)
        serializer = EmployeesSerializer(data=employee_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        employee_data=JSONParser().parse(request)
        employee = Employees.objects.get(employee_id=id)
        serializer = EmployeesSerializer(employee, data=employee_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        employee = Employees.objects.get(employee_id=id)
        employee.delete()
        return HttpResponse(status=204)


# upload_file 
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        file_name = file_obj.name
        file_path = 'media/' + file_name
        with open(file_path, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        return JsonResponse({'file_name': file_name})

        








            

