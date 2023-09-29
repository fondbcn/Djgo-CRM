from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    zipcode=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(f"{self.first_name}{self.last_name}")