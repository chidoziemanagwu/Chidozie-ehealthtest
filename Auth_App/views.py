import json
import requests
from . import forms
from pprint import pprint

# import quickemailverification

from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from os.path import join as join_path
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.views.generic import base as custom_views


# GET Current date and time.
# ---------------------------

Todays_Date = timezone.now()
Todays_Date = Todays_Date.strftime('%d th, %b %Y')


HealthUserModel = get_user_model()


class UsernameValidationView(custom_views.View):
    def post(self, request):

        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': '&#x25cf; username should only contain alphanumeric characters'}, status=400)

        if HealthUserModel.objects.filter(username=username).exists():
            return JsonResponse({'username_error': '&#x25cf; sorry username in use, choose another one'}, status=409)
        return JsonResponse({'username_valid': True})


class EmailValidationView(custom_views.View):
    def post(self, request):
        # client = quickemailverification.Client(
        #     settings.EMAIL_CHECKER_KEY)  # Replace API_KEY with your API Key
        # verifier_instance = client.quickemailverification()

        data = json.loads(request.body)
        email = data['email']

        url = "http://api.quickemailverification.com/v1/verify?email={0}&apikey={1}".format(
            email, settings.EMAIL_CHECKER_KEY)

        payload = {}

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'keep-alive',
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        email_data = response.json()

        try:
            email_valid_status = email_data['result']
        except:
            email_valid_status = 'inconclusive'

        # if not validate_email(email):
        #     return JsonResponse({'email_error': '&#x25cf; Email is invalid'}, status=400)

        if email_valid_status == 'invalid':
            # The response is in the body attribute
            return JsonResponse({'email_error': '&#x25cf; Email is invalid'}, status=400)
        elif email_valid_status == 'inconclusive':
            pass

        if HealthUserModel.objects.filter(email=email).exists():
            return JsonResponse({'email_error': '&#x25cf; sorry email in use, choose another one'}, status=409)
        return JsonResponse({'email_valid': True})


class AuthenticationError(custom_views.View):
    template_name = join_path(
        'Auth', 'authentication-error.html')

    def get(self, request):

        context = {
            'server_message': 'Oops!! Invalid login credentials.',
            'today': Todays_Date,
        }

        return render(request, self.template_name, context)


class DoctorRegisterView(custom_views.View):
    template_name = join_path('Auth', 'register_doctor.html')

    def post(self, request):
        form_class = forms.RegisterationForm(request.POST)
        profile_form_class = forms.DoctorProfileForm(request.POST)

        context = {
            'form': form_class,
            'profile_form': profile_form_class,
            'message': 'You are registered successfully !!',
        }
        try:
            if form_class.is_valid() and profile_form_class.is_valid():
                user = form_class.save(commit=False)
                # user.is_active = False
                user.save()
                # user profile save with user instance assigned.
                profile_form = profile_form_class.save(commit=False)
                profile_form.user = user
                profile_form.medical_practitioner = True
                profile_form.save()

                # reverse('mini-panel')
                return render(request, join_path('Auth', 'sign_up_success.html'), context)
        except Exception as Error:
            raise Error
        return render(request, self.template_name, context)

    def get(self, request):
        form_class = forms.RegisterationForm()
        profile_form_class = forms.DoctorProfileForm()
        context = {
            'form': form_class,
            'profile_form': profile_form_class,
            'message': 'You are registered successfully !!',
        }
        return render(request, self.template_name, context)


class UserRegisterView(custom_views.View):
    template_name = join_path('Auth', 'register_user.html')

    def post(self, request):
        form_class = forms.RegisterationForm(request.POST)
        profile_form_class = forms.UserProfileForm(request.POST)

        context = {
            'form': form_class,
            'profile_form': profile_form_class,
            'message': 'You are registered successfully !!',
        }
        try:
            if form_class.is_valid() and profile_form_class.is_valid():
                user = form_class.save(commit=False)
                # user.is_active = False
                user.save()
                # user profile save with user instance assigned.
                profile_form = profile_form_class.save(commit=False)
                profile_form.user = user
                profile_form.save()

                # reverse('mini-panel')
                return render(request, join_path('Auth', 'sign_up_success.html'), context)
        except Exception as Error:
            raise Error
        return render(request, self.template_name, context)

    def get(self, request):
        form_class = forms.RegisterationForm()
        profile_form_class = forms.UserProfileForm()
        context = {
            'form': form_class,
            'profile_form': profile_form_class,
            'message': 'You are registered successfully !!',
        }
        return render(request, self.template_name, context)


class UserLoginView(auth_views.LoginView):
    form_class = forms.LoginForm
    authentication_form = forms.LoginForm
    redirect_authenticated_user = True
    template_name = join_path('Auth', 'login.html')

    def form_valid(self, form):
        checkbox = form.cleaned_data['remember_me']
        return super().form_valid(form)


class UserLogoutView(auth_views.LogoutView):
    template_name = join_path('UserHealth', 'home.html')
    args = {'logout_message': 'You are now logged out !!'}
    extra_conext = args


class TestView(custom_views.View):
    # template_name = join_path(
    #     'master', 'Account_recovery', 'password_reset_confirmation.html')
    # template_name = join_path(
    #     'master', 'Account_recovery', 'password_reset_email_sent.html')
    # template_name = join_path(
    #     'master', 'Account_recovery', 'password_reset_complete.html')
    # template_name = join_path(
    #     'master', 'Change_password', 'password_change_done.html')
    template_name = join_path(
        'master', 'Account_confirmation', 'email_sent.html')

    def get(self, request):

        form_class = forms.UserOverridePasswordForm(user=request.POST)
        context = {
            'today': Todays_Date,
            'form': form_class,
        }

        return render(request, self.template_name, context)
