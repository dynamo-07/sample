from django.db import models
from django.db import *
from django.db import models

class employee(models.Model):
    employee_id = models.CharField(max_length=100) 
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.employee_id