from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    STATUS_CHOICES = [('pro', 'Pro'), ('simple', 'Simple')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='simple')

class Country(models.Model):
    country_name = models.CharField(max_length=100)

class Director(models.Model):
    director_name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.PositiveIntegerField()
    director_image = models.ImageField(upload_to='directors/')

class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.PositiveIntegerField()
    actor_image = models.ImageField(upload_to='actors/')

class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

class Movie(models.Model):
    STATUS_CHOICES = [('pro', 'Pro'), ('simple', 'Simple')]
    TYPES_CHOICES = [(144, '144p'), (360, '360p'), (480, '480p'), (720, '720p'), (1080, '1080p')]
    movie_name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    types = models.IntegerField(choices=TYPES_CHOICES, default=720)
    movie_time = models.PositiveIntegerField(help_text='Duration in minutes')
    description = models.TextField()
    movie_trailer = models.URLField(blank=True)
    movie_image = models.ImageField(upload_to='movies/')
    status_movie = models.CharField(max_length=6, choices=STATUS_CHOICES, default='simple')

class MovieLanguages(models.Model):
    language = models.CharField(max_length=50)
    video = models.FileField(upload_to='movie_languages/')
    movie = models.ForeignKey(Movie, related_name='languages', on_delete=models.CASCADE)

class Moments(models.Model):
    movie = models.ForeignKey(Movie, related_name='moments', on_delete=models.CASCADE)
    movie_moments = models.TextField()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField()  # Range 1 to 10, validation on serializer/form level
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, through='FavoriteMovie')

class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, related_name='favorite_movies', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)
