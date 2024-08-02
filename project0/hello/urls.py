from django.urls import path
from . import views


urlpatterns = [ 
    path("",views.one, name = "one"),
    path("<str:name>",views.greet, name ="greet")
    
]


 