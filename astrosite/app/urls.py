from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path("signin/", views.singin, name="signin"),
    path("signout/", views.signoutUser, name="logout"),
    path("signup/", views.signup, name="signup"),
]