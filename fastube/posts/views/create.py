from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.utils import youtube


class PostCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'posts/new.html',
                {
                    'site_name': 'New Post',
                }
        )

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        video_id = request.POST.get('video_id')
        content = request.POST.get('content')

        post = request.user.post_set.create(
                title=title,
                video_id=video_id,
                content=content,
        )

        return redirect('posts:new')


class PostCreateConfirmView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return redirect('posts:new')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        video_id = request.POST.get('video_id')
        content = request.POST.get('content')

        return render(
                request,
                'posts/confirm.html',
                {
                    'site_name': 'Confirm Post',
                    'title': title,
                    'video_id': video_id,
                    'content': content,

                    'youtube_original_url': youtube.get_youtube_original_url(video_id),
                    'youtube_embed_url': youtube.get_youtube_embed_url(video_id),
                    'youtube_thumbnail_url': youtube.get_youtube_thumbnail_url(video_id),
                }
        )
