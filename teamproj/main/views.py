from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from .models import Films
from .form import FilmsForm,ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    data = {
        'title': 'Smotri kino',
    }
    return render(request, 'main/index.html', data,)

def novinki(request):
    films = Films.objects.all()
    return render(request, 'main/novinki.html',{'films':films})

def create(request):
    error = ''
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novinki')
        else:
            error = 'Forma neverna'

    form = FilmsForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render (request, 'main/create.html',data)


def about(request):
    return render(request, 'main/about.html')

def melo(request):
    data2 = {
        'title': 'Melodrama',
    }
    return render(request, 'main/melo.html',data2)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =  request.POST.get('password')

            user = authenticate(request, username = username, password=password)

            if user is not None:
                login(request,user)
                redirect('index')
            else:
                messages.info(request, 'Username OR Password is incorrect')
            return redirect('index')

        context = {}
        return render(request, 'main/login.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request,'main/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'main/home.html')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form':form}
    return render(request, 'main/profile.html', context)
