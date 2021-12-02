from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView, DetailView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm
from .models import AstroPost

@login_required(login_url='signin')
def index(request):
    return render(request, "index.html")

def singin(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect!')
        context = {}
        return render (request, "accounts/signin.html", context)

def signoutUser(request):
    logout(request)
    messages.success(request, 'Come back soon!')
    return render(request,'signin.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'User {username} successfully registered')
                return redirect('signin')


        context = {'form': form}
        return render(request, "accounts/signup.html", context)  


class PostView(ListView):
    model = AstroPost
    template_name ='astro.html'