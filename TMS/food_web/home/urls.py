from django.urls import path,include
from . import views
app_name = "home"
urlpatterns=[
    path("SignUp/", views.SignUp, name="SignUp"),
    path("Login/", views.Login, name="Login"),
    path("Logout/", views.Logout, name="logout"),
    path("", views.home_page, name="home"),
    path("profile/", views.profile, name="profile"),
    path("contact/", views.home_page, name="contactus"),
]