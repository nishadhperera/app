from django.urls import path, re_path

from . import views

app_name = 'patient'

urlpatterns = [
    # /patient/
    path('', views.list_patients, name='home_patient'),
    # /patient/list
    path('list/', views.list_patients, name='list_patients'),
    # /patient/id
    path('<int:id>/', views.view_patient, name='view_patient'),
]
