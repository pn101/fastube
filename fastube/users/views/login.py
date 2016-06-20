from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'user/login.html',
                {
                    'site_name': 'Login Page',
                }
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next_page') or ('user:mypage')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(next_page)
        return redirect('user:login')
