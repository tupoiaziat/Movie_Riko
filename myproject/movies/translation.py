from .models import Country, Director, Actor, Genre, Movie, MovieLanguages
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class ProductTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Director)
class ProductTranslationOptions(TranslationOptions):
    fields = ('director_name', 'bio',)

@register(Actor)
class ProductTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'bio', )

@register(Genre)
class ProductTranslationOptions(TranslationOptions):
    fields = ('genre_name',)

@register(Movie)
class ProductTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')

@register(MovieLanguages)
class ProductTranslationOptions(TranslationOptions):
    fields = ('language',)






