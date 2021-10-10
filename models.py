from django.db import models
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    DateOfBirth=models.DateField(default=datetime.now)
    Status=models.BooleanField()
       

