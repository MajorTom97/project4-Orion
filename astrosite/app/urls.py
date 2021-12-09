from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostView, PostDetailView, PostCreateView, PostUpdatedView, PostDeleteView


urlpatterns = [
    path('', views.index, name='index'),
    path("signin/", views.singin, name="signin"),
    path("signout/", views.signoutUser, name="logout"),
    path("signup/", views.signup, name="signup"),

    path('profile/', views.accountSettings, name="profile"),
    
    # Paths for Astropost views
    path('astro/', PostView.as_view(), name="astro"),
    path('astro/<int:pk>', PostDetailView.as_view(), name="astro-detail"),
    path('astro/new', PostCreateView.as_view(), name="astro-create"),
    path('astro/<int:pk>/update/', PostUpdatedView.as_view(), name="astro-update"),
    path('astro/<int:pk>/delete', PostDeleteView.as_view(), name="astro-delete"),
    
    # Paths for News and static content
    path('news/', views.News, name="news"),
    path('reactions/<int:id_news>', views.ReactNews, name="ReactNews"),
    path('community/', views.community, name="community"),
]

