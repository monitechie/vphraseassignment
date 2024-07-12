from django.urls import path
from .views import top_gross_movies, top_votes_movies, top_rating_movies

urlpatterns = [
    path('movies/top-gross/', top_gross_movies, name='top-gross-movies'),
    path('movies/top-votes/', top_votes_movies, name='top-votes-movies'),
    path('movies/top-rating/', top_rating_movies, name='top-rating-movies'),
]
