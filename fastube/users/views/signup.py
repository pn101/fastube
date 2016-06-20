from django.views.generic import View
from django.shortcuts import render, redirect


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'auth/signup.html',
                {
                    'site_name': 'Signup Page',
                }
        )
