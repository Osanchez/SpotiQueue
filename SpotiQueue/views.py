from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from SpotiQueue.utility.SpotifyAPI import authorization_request


def home(request):
    return render(request, 'SpotiQueue/base.html')

def login(request):
    return render()

def authorize(request):
    response = redirect(authorization_request())
    return response


