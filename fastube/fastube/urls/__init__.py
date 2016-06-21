from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^', include('users.urls', namespace='user')),

] + static(settings.MEDIA_URL, documentroot=settings.MEDIA_ROOT)
