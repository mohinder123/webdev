from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("student", views.student, name="student"),
    path("driver", views.driver, name="driver"),
    path("request", views.request, name="request"),
    path("ongoing/<int:request_id>",views.ongoing, name="ongoing"),
    path("currentBookings", views.currentBookings, name = "currentBookings"),
    path("delete/<int:delete_id>", views.delete, name = "delete"),
    
    path("forgot-password", views.forgot_password, name="forgot_password"),
    path("reset-password/<str:username>", views.reset_password, name="reset_password"),
    
    
    
     
]
