"""imdb_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from authy.views import UserProfile, ReviewDetail, like, unlike, UserProfileMoviesWatched, UserProfileSeriesWatched, UserProfileWatchList, UserProfileMoviesReviewed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls')),
    path('actors/', include('actor.urls')),
    path('account/', include('authy.urls')),
    path('<username>/', UserProfile, name='profile'),
    path('<username>/movieswatched', UserProfileMoviesWatched, name='profile-movies-watched'),
    path('<username>/serieswatched', UserProfileSeriesWatched, name='profile-series-watched'),
    path('<username>/watchlist', UserProfileWatchList, name='profile-watch-list'),
    path('<username>/reviewed', UserProfileMoviesReviewed, name='profile-reviewed-list'),
    path('<username>/review/<imdb_id>', ReviewDetail, name='user-review'),
    path('<username>/review/<imdb_id>/like', like, name='user-review-like'),
    path('<username>/review/<imdb_id>/unlike', unlike, name='user-review-unlike'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
