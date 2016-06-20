from django.conf.urls import url

from users.views import *


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='users'),

]
