from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class Category(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.name}"
    
    
    
class Bid(models.Model):
    
    bid = models.FloatField(default=0)
    user = models.ForeignKey(User,on_delete= models.CASCADE, blank=True, null=True, related_name="bidding")
    
    def __str__(self):
        return f"{self.bid}"
    
 
 
class Balance(models.Model):
    
    balance = models.FloatField(default=0)
    user = models.OneToOneField(User,on_delete= models.CASCADE, blank=True, null=True, related_name="balance")
    
    def __str__(self):
        return f"{self.balance}"   

    
     
    


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=1000)
    price = models.ForeignKey(Bid, on_delete= models.CASCADE, blank=True, null=True, related_name="bidding")
    watchlist =  models.ManyToManyField(User, blank=True, null=True, related_name="watchlist")
    isactive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True, related_name="listing")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="listing")
    
    
    
    def __str__(self):
        return f"{self.title}"
    
     
        
    
    
    

