from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostView


urlpatterns = [
    path('', views.index, name='index'),
    path("signin/", views.singin, name="signin"),
    path("signout/", views.signoutUser, name="logout"),
    path("signup/", views.signup, name="signup"),
    
    # Paths for template views
    path('astro/', PostView.as_view(), name="astro"),
    path('news/', views.News, name="news"),
    path('reactions/<int:id_news>', views.ReactNews, name="ReactNews"),
    path('community/', views.community, name="community"),
]

