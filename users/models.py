import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    access_token = models.CharField(max_length=128)
    refresh_token = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.user.username} Profile'


class Playlist(models.Model):
    playlist_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique ID for this particular Playlist across entire site"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_creation_date = models.DateField(default=timezone.now, blank=True)
    playlist_name = models.CharField(max_length=128, help_text="Enter a title for the playlist")


class Contributors(models.Model):
    playlist_id = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True)
    contributor_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.contributor_id


class Genre(models.Model):
    genre = models.CharField(primary_key=True, unique=True, max_length=128)


class Song(models.Model):
    song_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique ID for this particular Song across entire site"
    )
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default=None)
    length = models.CharField(max_length=128)
    preview_link = models.CharField(max_length=128)


class SongInstance(models.Model):
    song_instance_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique ID for this particular Song Instance"
    )
    song_id = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True)
    playlist_id = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True)
    number_yes_votes = models.IntegerField(default=0)
    number_no_votes = models.IntegerField(default=0)
    adder_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.song_instance_id)

