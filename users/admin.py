from django.contrib import admin
from .models import Profile, Playlist, Contributor, Genre, Song, SongInstance
# Register your models here.

admin.site.register(Profile)
admin.site.register(Playlist)
admin.site.register(Contributor)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(SongInstance)

