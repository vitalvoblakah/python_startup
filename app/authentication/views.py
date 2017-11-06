from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from utils.utils import render_template

from .models import User
from .forms import LoginForm, RegisterForm


def auth_page(request):
    context = {
        'form': LoginForm
    }

    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')

    if request.method == "POST":
        context['form'] = LoginForm(request.POST)
        if context['form'].is_valid():

            user = authenticate(email=context['form'].cleaned_data['email'],
                                password=context['form'].cleaned_data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect('/home')

    return render_template(request, 'authenticate.html', context)


def register_page(request):
    context = {
        'form': RegisterForm
    }

    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')

    if request.method == "POST":
        context['form'] = RegisterForm(request.POST)
        if context['form'].is_valid():
            user = User.objects.create_user(email=context['form'].cleaned_data['email'],
                                            password=context['form'].cleaned_data['password'])

            if user:
                login(request, user)
                return HttpResponseRedirect('home')

    return render_template(request, 'register.html', context)

def logout(request):
    return