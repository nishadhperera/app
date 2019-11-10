from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import Doctor
from .serializers import DoctorSerializer


def list_doctors(request):
    all_doctors = Doctor.objects.all()
    context = {
        'all_doctors': all_doctors
    }
    return render(request, 'doctor/doctor_list.html', context)


# def view_doctor(request, id):
#     doctor = Doctor.objects.get(id=id)
#     return HttpResponse(
#         '<h2> ' + doctor.name + ' </h2>'
#         '<h3> ' + doctor.specialization + '</h3>'
#         '<body>' + doctor.address + '</body>'
#     )


def view_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    patient_list = doctor.registered_patients.all()

    context = {
        'doctor_info': doctor,
        'patient_list': patient_list,
    }
    return render(request, 'doctor/doctor_detail.html', context)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('reg_id', 'name')

