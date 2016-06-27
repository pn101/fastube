from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from fastube.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^api/', include('fastube.urls.api', namespace='api')),

    url(r'^', include('users.urls', namespace='user')),
    url(r'^posts/', include('posts.urls', namespace='posts')),

] + static(settings.MEDIA_URL, documentroot=settings.MEDIA_ROOT)
