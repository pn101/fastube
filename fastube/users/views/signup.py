from django.views.generic import View
from django.shortcuts import render, redirect

from users.models import User


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'user/signup.html',
                {
                    'site_name': 'Signup Page',
                }
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')

        user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                phonenumber=phonenumber,
        )

        return redirect('user:login')
