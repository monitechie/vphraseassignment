from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer


@api_view(['GET'])
def top_gross_movies(request):
    year = request.GET.get('year')
    movies = Movie.objects.filter(year=year).order_by('-gross')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_votes_movies(request):
    movies = Movie.objects.order_by('-votes')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_rating_movies(request):
    year = request.GET.get('year')
    movies = Movie.objects.filter(year=year).order_by('-rating')[:10]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
