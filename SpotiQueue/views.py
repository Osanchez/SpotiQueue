from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from SpotiQueue.utility.SpotifyAPI import authorization_request


def landing(request):
    return render(request, 'SpotiQueue/landing.html')


def dashboard(request):
    return render(request, 'SpotiQueue/dashboard.html')


def authorize(request):
    response = redirect(authorization_request())
    return response


