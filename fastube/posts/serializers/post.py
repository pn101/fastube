from rest_framework import serializers

from posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')

    class Meta:
        model = Post
        fields = [
            'pk',
            'username',
            'title',
            'content',
            'youtube_original_url',
            'created_at',
            'youtube_thumbnail_url',
        ]
