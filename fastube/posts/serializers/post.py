from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostModelSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'youtube_original_url',
            'created_at',
            'youtube_thumbnail_url',
            'pk',
        ]
