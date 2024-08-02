from django.contrib import admin
from .models import Category, Listing, Bid, User

admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(User)
 

# Register your models here.
