from django.conf.urls import url

from posts.api import *


urlpatterns = [
    url(r'^posts/$', PostListAPIView.as_view(), name='list'),
    url(r'^posts/(?P<slug>\w+)/comments/$', PostCommentListCreateAPIView.as_view(), name='comments'),

]
