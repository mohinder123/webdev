from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def one(request):
    return render(request, "hello/one.html")

def greet(request,name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })


    