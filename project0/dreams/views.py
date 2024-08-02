from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from django import forms

class newform(forms.Form):
    dream = forms.CharField(label="New Dream", widget=forms.TextInput(attrs={'placeholder':'Write your dreams here'}))
    

# Create your views here.
 

def index(request):
    if "dreams" not in request.session:
        request.session["dreams"] = []
        
    return render(request, "dreams/index.html",{
        "dreams": request.session["dreams"]
    })
    
def add(request):
    
    if request.method == "POST":
        form = newform(request.POST)
        if form.is_valid():
            dream = form.cleaned_data["dream"]
            request.session["dreams"] += [dream]
            return HttpResponseRedirect(reverse("dreams:index"))
            
        else:
            return render(request, "dreams/add.html",{
                "form":form
            })
        
    
    
    return render(request, "dreams/add.html",{
        "form" : newform()
    }) 