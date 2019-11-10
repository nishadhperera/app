from django.urls import path, re_path, include
from rest_framework import routers

from doctor.views import DoctorViewSet

router = routers.DefaultRouter()
router.register(r'', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
