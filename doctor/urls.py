from django.urls import path, re_path, include
from rest_framework import routers

from . import views

app_name = 'doctor'

router = routers.DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)

urlpatterns = [
    path('', views.list_doctors, name='home_doctors'),
    # /doctor/list
    path('list/', views.list_doctors, name='list_doctors'),
    # /doctor/id
    path('<int:id>/', views.view_doctor, name='view_doctor'),
    # doctor list API
    path('api/', include(router.urls))
]
