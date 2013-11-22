# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from registration.forms import *
from django.contrib import auth


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/authentication')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def authenticate(request):
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            if form.get_user():
                auth.login(request, form.get_user())
                return HttpResponseRedirect('/library/books/')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication.html', {'form': form})
