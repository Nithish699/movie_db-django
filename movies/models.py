from django.db import models
from django.urls import reverse

class Movie(models.Model):
    movie_name = models.CharField(max_length=255)  # Movie Name
    year_of_release = models.IntegerField()  # Year of Release
    watch_time = models.IntegerField()  # Watch Time (in minutes)
    movie_rating = models.DecimalField(max_digits=3, decimal_places=1)  # Movie Rating
    metascore = models.IntegerField()  # Metascore of movie
    gross = models.DecimalField(max_digits=10, decimal_places=2)  # Gross earnings (in millions)
    votes = models.IntegerField()  # Votes
    description = models.TextField()  # Description


    def __str__(self):
        return self.movie_name
    
    def get_absolute_url(self):
        return reverse('movie_detail', args=[self.id])