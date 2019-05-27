from django.shortcuts import render
from django.http import HttpResponse

from .models import Patient


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