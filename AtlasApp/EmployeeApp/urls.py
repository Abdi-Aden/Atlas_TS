from django.urls import path
from EmployeeApp import views


# EmployeeApp/urls.py
urlpatterns = [
    path(r'^departments/$', views.departmentApi),
    path(r'^departments/(?P<id>[0-9]+)/$', views.departmentApi),

    path(r'^employees/$', views.employeeApi),
    path(r'^employees/(?P<id>[0-9]+)/$', views.employeeApi),

    path(r'^vehicles/$', views.vehicleApi),
    path(r'^vehicles/(?P<id>[0-9]+)/$', views.vehicleApi),


    ]