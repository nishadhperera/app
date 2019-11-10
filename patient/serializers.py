from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'
        # fields = ('name',
        #           'nic',
        #           'age',
        #           'date_of_birth',
        #           'email',
        #           'address',
        #           'mobile_number',
        #           'gp',
        #           )
        depth = 1
