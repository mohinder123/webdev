from django.contrib import admin
from .models import User, Student, Driver, Request, Location, Distance, UserSecurityAnswer

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Driver)
admin.site.register(Request)
admin.site.register(Location)
admin.site.register(Distance)

@admin.register(UserSecurityAnswer)
class UserSecurityAnswerAdmin(admin.ModelAdmin):
    list_display = ("user", "answer")

# Register your models here.
