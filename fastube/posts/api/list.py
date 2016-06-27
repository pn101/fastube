import json

from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post


class PostListAPIView(APIView):

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
        return Response(data)
