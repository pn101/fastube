import json
from django.views.generic import View
from django.http.response import HttpResponse

from posts.models import Post


class PostListAPIView(View):

    def get(self, request, *args, **kwargs):
        data = [
            {
                'title': post.title,
                'content': post.content,
                'youtube_original_url': post.youtube_original_url,
                'created_at': str(post.created_at),
            }
            for post
            in Post.objects.all()
        ]
        return HttpResponse(
                json.dumps(data),
                content_type='application/json',
        )
