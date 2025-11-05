from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name',]

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name',]

class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']

class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']

class RatingSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M', read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'user', 'parent', 'stars', 'text', 'created_date']

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    favorite_movies = FavoriteMovieSerializer(many=True, read_only=True, source='favorite_movies')
    class Meta:
        model = Favorite
        fields = ['user', 'favorite_movies']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'movie_image', 'movie_name', 'year', 'country', 'genres', 'status_movie']

class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    director = DirectorSerializer(read_only=True)
    moments_frame = MomentsSerializer(many=True, read_only=True)
    languages = MovieLanguagesSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['movie_image', 'movie_name', 'year', 'country',
                  'genres', 'director',
                  'actors', 'types', 'movie_time',
                  'description', 'movie_trailer', 'status_movie', 'moments_frame', 'languages', 'ratings']