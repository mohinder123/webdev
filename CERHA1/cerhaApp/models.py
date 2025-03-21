from django.db import models
from typing import Any
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



class User(AbstractUser):
    isStudent = models.BooleanField(default=False)
    isDriver = models.BooleanField(default=False)
    
class Location(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}" 
    
    
class Distance(models.Model):
    start = models.ForeignKey(Location, on_delete= models.CASCADE, blank=True, null=True, related_name="distance1")
    end = models.ForeignKey(Location, on_delete= models.CASCADE, blank=True, null=True, related_name="distance2")
    distance = models.IntegerField()
    def __str__(self):
        return f"{self.start} to {self.end}" 
     


class Student(models.Model):
    
    rollNo = models.IntegerField(primary_key=True, max_length=9, unique=True)
    email = models.EmailField(default="student@gmail.com", max_length=254)
    location = models.ForeignKey(Location, on_delete= models.CASCADE, blank=True, null=True, related_name="student")
    user = models.OneToOneField(User,on_delete= models.CASCADE, blank=True, null=True, related_name="student")
    
    def __str__(self):
        return f"{self.user.username}"  
    
    
    
class Driver(models.Model):
    
    
    vehicleNo = models.IntegerField(primary_key=True, max_length=9, unique=True)
    location = models.ForeignKey(Location, on_delete= models.CASCADE, blank=True, null=True, related_name="driver")
    phn = models.CharField(
        max_length=10,
        validators=[RegexValidator(
            regex='^\d{10}$',
            message='Phone number must be exactly 10 digits.',
            code='invalid_phone_number'
        )]
    )
    user = models.OneToOneField(User,on_delete= models.CASCADE, blank=True, null=True, related_name="driver")
    
    
    def __str__(self):
        return f"{self.user.username}"  
    
    
class Request(models.Model):
    student = models.OneToOneField(Student, on_delete= models.CASCADE, blank=True, null=True, related_name="requests")
    isAccepted = models.BooleanField(default=False)
    time = models.TimeField(auto_now=True)
    driver = models.ForeignKey(Driver, on_delete= models.CASCADE, blank=True, null=True, related_name="requests")
    time_taken = models.FloatField(default= 0.00)
    status = models.CharField(max_length=20, default='Pending')  
    
    
    
class UserSecurityAnswer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="security_answer")
    answer = models.CharField(max_length=255)  # Store each user's answer to the common question

    def __str__(self):
        return f"Security answer for {self.user.username}"
    


