from django.db import models
from django.contrib.auth.models import User

#TODO: create database tables to hold user information and playlist information(tokens, songs added to playlists, playlist contributors)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    access_token = models.CharField(max_length=128)
    refresh_token = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.user.username} Profile'


class Playlist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contributors = models.ForeignKey(User, on_delete=models.SET_NULL)

class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField()
    genre =
    length =
    preview_link =

