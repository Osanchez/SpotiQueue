from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from SpotiQueue.utility.SpotifyAPI import authorization_request
from users.models import Profile


def landing(request):
    return render(request, 'SpotiQueue/landing.html')


@login_required
def dashboard(request):

    context = {
        'authenticated': False,
        'profile': None
    }

    if Profile.objects.filter(user=request.user).exists():
        context['authenticated'] = True
        context['profile'] = Profile.objects.filter(user=request.user)
        print("profile exists")
    else:
        print("profile does not exists")

    return render(request, 'SpotiQueue/dashboard.html', context)


def authorize(request):
    response = redirect(authorization_request())
    return response


