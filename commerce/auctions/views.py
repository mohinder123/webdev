from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Category, Listing, Bid


def index(request):
    return render(request, "auctions/index.html",{
        "listings": Listing.objects.filter(isactive = True)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    


@login_required(login_url= 'login' )
def listing(request):
    if request.method == "POST":
        
        listing = Listing()
        currentuser = request.user
        
        bid = Bid(bid=float(request.POST["price"]), user = currentuser)
        bid.save()
        listing.title = request.POST["title"]
        listing.description = request.POST["description"]
        listing.image = request.POST["image"]
        listing.category = Category.objects.get(pk = int(request.POST["cat"]))
        listing.price = bid
        listing.owner = currentuser
        listing.save()
        return HttpResponseRedirect(reverse("index"))
        
    return render(request, "auctions/listing.html", {
        "categorys": Category.objects.all()
    })
    

def category(request):
    return render(request, "auctions/category.html", {
        "categorys": Category.objects.all()
    })
    
    
    
def catlist(request, category_id):
    category = Category.objects.get(pk = category_id)
    return render(request, "auctions/catlist.html",{
        "category": category,
        "listings": category.listing.all()
    })
    
    
@login_required(login_url= 'login' )
def watchlist(request):
    currentuser = request.user
    return render(request, "auctions/watchlist.html",{
        "items": currentuser.watchlist.all()
    })



 
 

def item(request, listing_id):
    item = Listing.objects.get(pk = listing_id)
    highbid = item.price
    remove = False
    currentuser = request.user
    
    if request.user in item.watchlist.all():
        iswatchlist = True
    else:
        iswatchlist = False
            
    if request.method == "POST":
         
        if float(request.POST["bid"]) > float(item.price.bid):
            highbid = Bid(bid = float(request.POST["bid"]), user = request.user)
            highbid.save()
            item.price = highbid
            item.save()
            
        else:
            pass
        
    if item.owner == currentuser:
        remove = True
    else:
        remove = False
            
    return render(request, "auctions/item.html",{
        "item": item,
        "iswatchlist":iswatchlist,
        "highbid":highbid,
        "remove":remove,
        "currentuser":currentuser,
        "itemIsActive":item.isactive
    })
    
    
def addWatchlist(request, item_id):
    item = Listing.objects.get(pk = item_id)
    currentuser = request.user
    item.watchlist.add(currentuser)
    return HttpResponseRedirect(reverse("item", args=[item.id]))


def removeWatchlist(request, item_id):
    item = Listing.objects.get(pk = item_id)
    currentuser = request.user
    item.watchlist.remove(currentuser)
    return HttpResponseRedirect(reverse("item", args=[item.id]))



def removeItem(request, item_id):
    item = Listing.objects.get(pk = item_id)
    currentuser = request.user
    if(item.isactive == True):
        item.isactive = False
        
    else:
        item.isactive = True
        
    item.save()
    return HttpResponseRedirect(reverse("item", args=[item.id]))
    
        
        
    
    


 
    


 
    
        
        
    


