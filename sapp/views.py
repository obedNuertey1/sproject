from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import SModel
from django.db import connection
from django.db.models import Q
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def homePage(request):
    data = SModel.objects.all()
    context = {'data': data}
    return render(request, 'sapp/HomePage.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('sapp-homepage')
    return render(request, 'sapp/Login.html')


def profile(request):
    form = CreateUserForm()
    if request.method == 'POST':
        return redirect('sapp-homepage')
    else:
        form = CreateUserForm()
    return render(request, 'sapp/profile.html', {'form': form})


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('first_name')
            form.save()
            messages.success(request, f'Account was created for {user}')
            return redirect('sapp-loginPage')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'sapp/signup.html', context)


def terms(request):
    return render(request, 'sapp/terms.html')


def welcome(request):
    return render(request, 'sapp/welcome.html')


def view_pdf(request):
    return render(request, 'sapp/view_pdf.html')
