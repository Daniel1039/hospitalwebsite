from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.http import request
# Create your models here.

class Appointment(models.Model):
    PURPOSE_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Orthopedics', 'Orthopedics'),
        ('Neurology', 'Neurology'),
        ('Radiology', 'Radiology'),
        ('Surgery', 'Surgery'),
        ('Other', 'Other'),
    ]
    
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    department= models.CharField(max_length=50, choices=PURPOSE_CHOICES, default='Other')
    request= models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted= models.BooleanField(default=False)
    accepted_date= models.DateField(auto_now_add=False, null=True, blank=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]
        
# myapp/models.py


# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

# settings.py

