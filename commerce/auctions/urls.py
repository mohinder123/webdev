from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing", views.listing, name = "listing"),
    path("category", views.category, name = "category"),
    path("category/<int:category_id>", views.catlist, name = "catlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("item/<int:listing_id>", views.item, name="item"),
    path("removeWatchlist/<int:item_id>", views.removeWatchlist, name="removeWatchlist"),
    path("addWatchlist/<int:item_id>", views.addWatchlist, name="addWatchlist"),
    path("removeItem/<int:item_id>", views.removeItem, name="removeItem"),
    path("balance", views.balance, name="balance")
    
    
]
