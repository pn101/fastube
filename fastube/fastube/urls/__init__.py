from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from users.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('fastube.urls.users', namespace='users')),

] + static(settings.MEDIA_URL, documentroot=settings.MEDIA_ROOT)
