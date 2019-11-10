"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MMS Open API",
      default_version='v1',
      description="Interface to exchange MMS data",
   ),
   public=True,
)

urlpatterns = [
    re_path(r'^articles/', include('articles.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^doctor/', include('doctor.urls')),
    re_path(r'^patient/', include('patient.urls')),
    re_path(r'^admin/', admin.site.urls),

    # API urls
    re_path(r'^api/doctor/', include('doctor.api.urls')),
    re_path(r'^api/patient/', include('patient.api.urls')),

    re_path(r'^api/swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
