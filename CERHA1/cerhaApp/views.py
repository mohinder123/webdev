from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Student, Driver, Request, Location, Distance, UserSecurityAnswer
import datetime
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages


SECURITY_QUESTION = "What is your Mother's full name?"
 

def index(request):
        currentuser = request.user
        
        if not currentuser.isStudent and not currentuser.isDriver:
            return HttpResponseRedirect(reverse("login"))
        elif(currentuser.isStudent and not currentuser.isDriver):
            return HttpResponseRedirect(reverse("student"))
        elif(not currentuser.isStudent and currentuser.isDriver):
            return HttpResponseRedirect(reverse("driver"))
    


 
    
             
 
    
    
    
def student(request):
    currentuser = request.user
    locations = Location.objects.all()
    location_id = request.POST.get("location")
    if(not currentuser.isStudent):
        currentuser.isStudent = True
        currentuser.save()
    
    if request.method == "POST": 
        rollNo = request.POST["rollNo"]
        email = request.POST["email"]
        x = False
        student = Student() 
        
        for all in Student.objects.all():
            if(all.rollNo == rollNo and all.user == currentuser):
                student = all
                student.location = Location.objects.get(id=location_id)
                student.save()
                x = True
                break        
              
        if(not x): 
            student.rollNo = request.POST["rollNo"]
            student.email = request.POST["email"]
            
            student.user = currentuser
            student.location = Location.objects.get(id=location_id)
            try:
                student.save() 
            except IntegrityError:
                message = (
                    "Enter your own roll number"
                )   
                return render(request, "cerhaApp/404.html", {'error_message': message}, status=404)
            
        req = Request()
        req.student = student
        try:
            req.save()
            return HttpResponseRedirect(reverse("request"))
        except IntegrityError:
                message = (
                    "You Already Have a Ride"
                )   
                return render(request, "cerhaApp/404.html", {'error_message': message}, status=404)
    else:
        return render(request, "cerhaApp/student.html",{
            "locations" : locations,
            "currentuser" : currentuser
    })
    
     
    
    
   
def driver(request):
    currentuser = request.user
    locations = Location.objects.all()
    location_id = request.POST.get("location")

    if not currentuser.isDriver:
        currentuser.isDriver = True
        currentuser.save()

    if request.method == "POST":
        vehicleNo = request.POST.get("vehicleNo", "").strip()
        phn = request.POST.get("phn", "").strip()

        
        if len(phn) != 10 or not phn.isdigit():
            message = "Error: Phone number must be exactly 10 digits."
            return render(request, "cerhaApp/404.html", {'error_message': message}, status=404)
 
        if phn == '0000000000' or phn.startswith('0') or len(set(phn)) == 1:  
            message = "Error: Phone number cannot be all zeros, start with a zero, or be made up of the same digit."
            return render(request, "cerhaApp/404.html", {'error_message': message}, status=404)

        
        existing_driver = Driver.objects.filter(vehicleNo=vehicleNo).first()
        if existing_driver and existing_driver.user != currentuser:
            message = "Error: A driver with this vehicle number already exists."
            return render(request, "cerhaApp/404.html", {'error_message': message}, status=404)

        
        try:
            driver, created = Driver.objects.get_or_create(user=currentuser, vehicleNo=vehicleNo)
        except IntegrityError:
            message = "Error: Enter your own Vehicle Number"
            return render(request, "cerhaApp/404.html", {'error_message': message}, status=404)
 
        driver.phn = phn
        driver.location = Location.objects.get(id=location_id)

        try:
            driver.full_clean()   
            driver.save()   
            return HttpResponseRedirect(reverse("request"))
        except ValidationError as e:
            print(f"ValidationError: {e.message_dict}")  # For debugging purposes
            message = f"Validation Error: {e.message_dict.get('phn', ['Invalid data'])[0]}"
            return render(request, "cerhaApp/404.html", {'error_message': message}, status=404)
        except IntegrityError:
            message = "Error: Database Integrity Issue"
            return render(request, "cerhaApp/404.html", {'error_message': message}, status=404)

    return render(request, "cerhaApp/driver.html", {
        "locations": locations,
        "currentuser": currentuser
    })
    
    
    
def request(request):
    currentuser = request.user
    if currentuser.isStudent:
        try:
            stu = Student.objects.get(user = currentuser)
            req = Request.objects.get(student = stu)
            return render(request, "cerhaApp/request.html",{
                "req" : req,
                "currentuser" : currentuser
            })
            
     
        except Request.DoesNotExist:
            
            message = (
            "No Requests"
            )
            
            
            return render(request, "cerhaApp/404.html", {'error_message': message}, status=404)
        
    elif currentuser.isDriver:
        req = Request.objects.all()
        return render(request, "cerhaApp/request.html",{
                "req" : req,
                "currentuser" : currentuser
            })
   
    
    
    
    

    
    
    
def ongoing(request, request_id):
    
    currentuser = request.user
    req = Request.objects.get(pk = request_id)
    requests = Request.objects.all()
    req.isAccepted = True
    if currentuser.isDriver:
        req.driver = Driver.objects.get(user = currentuser)
            
    
    
    
    distances = Distance.objects.all()
    for all in distances :
        if (all.start == req.student.location and all.start == req.driver.location) :
            req.time_taken = 0
        elif (all.end == req.student.location and all.end == req.driver.location) :
            req.time_taken = 0
        elif (all.start == req.student.location or all.start == req.driver.location): 
            if(all.end == req.student.location or all.end == req.driver.location):
                req.time_taken = all.distance*0.004
                break
    
    req.save()
    return HttpResponseRedirect(reverse("currentBookings"))
    
    
                    
        
    

     
    
def currentBookings(request):
    requests = Request.objects.all()
    currentuser = request.user
    
    if currentuser.isDriver:
        d = Driver.objects.get(user = currentuser)
    
    return render(request, "cerhaApp/ongoing.html",{
        "requests" : requests,
        "currentuser" : currentuser,
        "d": d
    })
    
    
    
def delete(request, delete_id):
    currentuser = request.user
    del_req = Request.objects.get(pk = delete_id)
    del_req.delete()
    if currentuser.isStudent:
        return HttpResponseRedirect(reverse("request"))
    elif currentuser.isDriver:
        return HttpResponseRedirect(reverse("currentBookings"))
        
    
    
        
    


def login_view(request):
    if request.method == "POST":

         
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

         
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "cerhaApp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "cerhaApp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        selection = request.POST["selection"]
        security_answer = request.POST.get("security_answer")

         
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "cerhaApp/register.html", {
                "message": "Passwords must match."
            })

         
        try:
            user = User.objects.create_user(username, email, password)
            UserSecurityAnswer.objects.create(user=user, answer=security_answer)
            if (selection == "Driver"):
                user.isDriver = True
            if (selection == "Student"):
                user.isStudent = True
                
             
            
            
            user.save()
        except IntegrityError:
            return render(request, "cerhaApp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "cerhaApp/register.html")
    
    


User = get_user_model()

def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = User.objects.filter(username=username).first()

        if user and hasattr(user, "security_answer"):
            return redirect("reset_password", username=username)
        else:
            messages.error(request, "User not found or no security answer set!")
            return redirect("forgot_password")

    return render(request, "forgot_password.html")



def reset_password(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        security_answer = request.POST.get("security_answer")
        new_password = request.POST.get("new_password")

        # Validate the security answer
        if user.security_answer.answer.strip().lower() == security_answer.strip().lower():
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password reset successful! Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Security answer is incorrect.")
            return redirect("reset_password", username=username)

    return render(request, "reset_password.html", {"user": user, "security_question": SECURITY_QUESTION})
    



# Create your views here.
