from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class MyPageView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'user/mypage.html',
                {
                    'site_name': 'MyPage',
                }
        )
