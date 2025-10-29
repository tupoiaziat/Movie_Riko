from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieViewSet, ActorViewSet, DirectorViewSet, CountryViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
