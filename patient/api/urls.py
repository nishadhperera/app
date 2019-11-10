from django.urls import path, re_path, include
from rest_framework import routers

from patient.views import PatientViewSet

router = routers.DefaultRouter()
router.register(r'', PatientViewSet)

urlpatterns = [
    path('', include(router.urls))
]
