from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm, loginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as lgt
from django.contrib.auth import login as lgn


def registration(request):
    if request.method == "POST":
        user_form = RegistrationForm(data=request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            User.objects.create_user(**user_form.cleaned_data)
            user = authenticate(username=user_form.cleaned_data.get('username'),
                                password=user_form.cleaned_data.get('password'))
            lgn(request,user)
            return redirect('home')
        else:
            return HttpResponse('<h1>Данные не валидны!</h1>')
    context = {
        'form': RegistrationForm(),
    }
    return render(request, 'accounts/registration.html', context)


def login(request):
    if request.method == "POST":
        user_form = RegistrationForm(data=request.POST)
        print(user_form.data)
        user = authenticate(username=user_form.data.get('username'),
                            password=user_form.data.get('password'))
        lgn(request, user)
        return redirect('home')
    context = {
        'form': loginForm(),
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    lgt(request)
    return redirect('home')
