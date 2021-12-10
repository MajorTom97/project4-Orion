from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import requests

# Create your views here.
from .forms import CreateUserForm, profileForm
from .models import AstroPost, News as NewsModel, userSetting

@login_required(login_url='signin')
def index(request):
    blogNews = []
    try:
        response = requests.get("https://api.spaceflightnewsapi.net/v3/blogs?_limit=3")
        blogNews = response.json()
        print(blogNews)
    except:
        print("---------Upsss----------")
    context = {"blogNews": blogNews}
    return render(request, "index.html", context)

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
    return render(request,'signout.html')

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
    context_object_name = 'posts'
    oredering = ['-date_posted']
    context = {
        'posts': AstroPost.objects.all()
    }

class PostDetailView(DetailView):
    model = AstroPost

class PostCreateView(LoginRequiredMixin, CreateView):
    model = AstroPost
    fields = ['post', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdatedView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AstroPost
    fields = ['post', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        AstroPost = self.get_object()
        if self.request.user == AstroPost.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AstroPost
    success_url = '/astro'

    def test_func(self):
        AstroPost = self.get_object()
        if self.request.user == AstroPost.author:
            return True
        return False

# Astronomy News

def News(request):
    apinews = []
    try:
        response = requests.get("https://api.spaceflightnewsapi.net/v3/articles?_limit=10")
        apinews = response.json()
    
    except:
        print("ERROR")
    context = {"apinews": apinews}
    return render(request, "news.html", context)

def ReactNews(request, id_news):
    notice = NewsModel.objects.filter(id_news=id_news).first()
    if not notice:
        notice = NewsModel.objects.create(id_news=id_news)
    if not NewsModel.objects.filter(id_news=id_news, reactions=request.user).first():
        notice.reactions.add(request.user)
    
    return JsonResponse({
        "id_news":id_news,
        "reactions":notice.reactions.count()
    })

@login_required(login_url='signin')
def accountSettings(request):
    userSetting = request.user.userSetting
    form = profileForm(instance=userSetting)

    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=userSetting)
        if form.is_valid():
            form.save
    
    context={'form':form}
    return render(request, "accounts/profile.html", context)

def community(request):
    context = {}
    return render(request, "community.html", context)