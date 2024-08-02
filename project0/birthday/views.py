from django.shortcuts import render
import datetime




def index(request):
    now = datetime.datetime.now()
    
    return render(request,"birthday/index.html", {
        "birthday": now.month == 10 and now.day == 17
    })
    

        
      