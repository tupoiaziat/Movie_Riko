from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = '__all__'

class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

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

class MovieSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    director = DirectorSerializer()
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)
    languages = MovieLanguagesSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
