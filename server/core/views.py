from django.shortcuts import render, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.decorators import api_view
from .forms import CustomUserCreationForm

# Create your views here.

def register_user(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = CustomUserCreationForm()
        print(form.errors)

    return render(request, 'core/register.html', {'form': form})