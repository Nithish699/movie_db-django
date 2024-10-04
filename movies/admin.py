from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'year_of_release', 'movie_rating', 'gross')
    search_fields = ('movie_name',)
    list_filter = ('year_of_release', 'movie_rating')

admin.site.register(Movie, MovieAdmin)
