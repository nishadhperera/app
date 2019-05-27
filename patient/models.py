from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=30)
    nic = models.CharField(max_length=20, unique=True)
    age = models.DecimalField(max_digits=5, decimal_places=0)
    date_of_birth = models.DateField(default=None)
    email = models.EmailField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile_number = models.CharField(max_length=20,null=True)
    created_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
