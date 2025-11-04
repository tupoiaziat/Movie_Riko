from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieListAPIView, MovieDetailAPIView, ActorViewSet, DirectorViewSet, CountryViewSet, GenreViewSet
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

router = DefaultRouter()
router.register(r'actors', ActorViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = i18n_patterns(
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('movie/', MovieListAPIView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
