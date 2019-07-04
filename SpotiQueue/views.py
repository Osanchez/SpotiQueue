from django.shortcuts import render, redirect
from SpotiQueue.utility.SpotifyAPI import authorization_request


def home(request):
    return render(request, 'SpotiQueue/main.html')


def authorize(request):
    response = redirect(authorization_request())
    return response


