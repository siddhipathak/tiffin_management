from django.urls import path
from . import views
app_name = "shop"
urlpatterns = [
path("", views.index, name="shopHome"),
path("about/", views.about, name="aboutus"),
path("tracker/", views.tracker, name="trackingstatus"),
path("search/", views.search, name="search"),
path("products/<int:myid>", views.productview, name="productview"),
path("prodview1/", views.prodview1, name="prodview1"),
path("checkout/", views.checkout, name="checkout"),
]