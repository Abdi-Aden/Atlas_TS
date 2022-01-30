
   
from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django import settings

# EmployeeApp/urls.py
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^departments/$', views.departmentApi),
    url(r'^departments/(?P<id>[0-9]+)/$', views.departmentApi),

    url(r'^employees/$', views.employeeApi),
    url(r'^employees/(?P<id>[0-9]+)/$', views.employeeApi),

    url(r'^vehicles/$', views.vehicleApi),
    url(r'^vehicles/(?P<id>[0-9]+)/$', views.vehicleApi),

    url(r'^admin/', views.admin, name='admin'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^Employee/SaveFile$', views.saveFile, name='saveFile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)