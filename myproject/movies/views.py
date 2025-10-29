from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie, Actor, Director, Country, Genre
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer, CountrySerializer, GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'country__country_name': ['exact'],
        'year': ['gte', 'lte'],
        'genres__genre_name': ['exact'],
        'status_movie': ['exact'],
        'actors__actor_name': ['exact'],
        'director__director_name': ['exact'],
    }
    search_fields = ['movie_name']
    ordering_fields = ['year']

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'actor_name': ['exact', 'icontains'],
        'age': ['gte', 'lte'],
    }
    search_fields = ['actor_name']
    ordering_fields = ['age', 'actor_name']

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'director_name': ['exact', 'icontains'],
        'age': ['gte', 'lte'],
    }
    search_fields = ['director_name']
    ordering_fields = ['age', 'director_name']

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'country_name': ['exact', 'icontains'],
    }
    search_fields = ['country_name']

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'genre_name': ['exact', 'icontains'],
    }
    search_fields = ['genre_name']
