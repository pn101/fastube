from django.views.generic import View
from django.shortcuts import render


class MyPageView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'user/mypage.html',
                {
                    'site_name': 'MyPage',
                }
        )
