from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Thread, Reply, Profile
from django.contrib.auth.decorators import login_required
from .forms import ThreadForm, UserRegistrationForm, ReplyForm
from .forms import UserRegistrationForm
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout

def index(request):
    threads = Thread.objects.all()
    return render(request, "threads/index.html", {"threads": threads[::-1]})

@login_required
def thread_create(request):
    if request.method == "POST":
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True, author=request.user)
            # thread.author = request.user
            # thread.save()
            messages.success(request, 'Thread created successfully!')
            print("All OK! THREAD CREATED!")
            return redirect('/')
    else:
        form = ThreadForm()
    return render(request, 'threads/create_thread.html', {'form': form})

def post_detail(request, id):
    thread = Thread.objects.get(id=id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save(commit=True, author=request.user, thread=thread)
            return redirect(f'/posts/{id}')
    else:
        return render(request, "threads/post_detail.html", {"thread": thread})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            print("Invalid User!")
            print(form.errors)
            messages.error(request, form.errors)

            return render(request, "threads/register.html", {"form":form})
            #todo add an error page
    else:
        form = UserRegistrationForm()
        return render(request, "threads/register.html", {"form":form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("Invalid User!")
            messages.error(request, "Your user is WRONG!")
            return render(request, "threads/login.html")
            # todo add an error page
    else:
        return render(request, "threads/login.html")

def user_logout(request):
    logout(request)
    #todo add a logout button somewhere
    return redirect('/')

def profile_detail(request, id):
    profile = Profile.objects.get(id=id)
    return render(request, "threads/profile_detail.html", {"profile": profile})