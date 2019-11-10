from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Patient
from .models import Doctor
from .serializers import PatientSerializer


def list_patients(request):
    all_patients = Patient.objects.all()
    context = {
        'all_patients': all_patients
    }
    return render(request, 'patient/patient_list.html', context)


def view_patient(request, id):
    patient = Patient.objects.get(id=id)
    return HttpResponse(
        '<h2> ' + patient.name + ' </h2>'
        '<h3> ' + patient.mobile_number + '</h3>'
        '<body>' + patient.address + '</body>'
    )


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
