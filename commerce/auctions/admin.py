from django.contrib import admin
from .models import Category, Listing, Bid, User, Balance

admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(User)
admin.site.register(Balance)
 

# Register your models here.
