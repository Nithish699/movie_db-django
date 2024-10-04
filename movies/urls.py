from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.movie_search, name='movie_search'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
]
