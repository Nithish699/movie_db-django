from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
from fuzzywuzzy import process
from django.views.generic import DetailView


def movie_list(request):
    movies = Movie.objects.all()  # Fetch all movies from the database
    return render(request, 'movie_list.html', {'movies': movies})

def movie_search(request):
    movie_name = request.GET.get('movie_name', '')
    year_of_release = request.GET.get('year_of_release')
    movie_rating = request.GET.get('movie_rating')

    movies = Movie.objects.all()

    if movie_name:
        movies = movies.filter(movie_name__icontains=movie_name)
    if year_of_release:
        movies = movies.filter(year_of_release=year_of_release)
    if movie_rating:
        if movie_rating == 'below_8':
            movies = movies.filter(movie_rating__lt=8)
        elif movie_rating == '8_9':
            movies = movies.filter(movie_rating__gte=8, movie_rating__lt=9)
        elif movie_rating == '9_10':
            movies = movies.filter(movie_rating__gte=9, movie_rating__lte=10)

    context = {'movies': movies}
    return render(request, 'movie_search.html', context)




def autocomplete(request):
    if 'term' in request.GET:
        term = request.GET.get('term')
        # Fetch all movie names from the database
        movie_names = Movie.objects.values_list('movie_name', flat=True)
        # Get fuzzy matches
        matches = process.extract(term, movie_names, limit=15)  # Adjust limit as needed
        # Return the matched movie names
        results = [match[0] for match in matches]
        return JsonResponse(results, safe=False)
    
    return JsonResponse([], safe=False)

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'