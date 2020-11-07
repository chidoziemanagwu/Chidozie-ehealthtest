from . import forms
from . models import *
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse
from os.path import join as join_path
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.views.generic import base as custom_views

from django.shortcuts import render, redirect, HttpResponse

HealthUserModel = get_user_model()

# GET Current date and time.
# ---------------------------

Todays_Date = timezone.now()
Todays_Date = Todays_Date.strftime('%d th, %b %Y')


# GET Patients count per illness.
# --------------------------------

ebola_patients = UserHealthInfo.objects.filter(ebola_status=True).count()
malaria_patients = UserHealthInfo.objects.filter(malaria_status=True).count()
previous = UserHealthInfo.objects.filter(previous=True).count()

female_users = UserHealthInfo.objects.filter(Gender='female').count()
male_users = UserHealthInfo.objects.filter(Gender='male').count()
all_user_data = UserHealthInfo.objects.all().reverse()
all_users = HealthUserModel.objects.all().count()


class MiniPanelView(custom_views.View):
    template_name = join_path(
        'UserHealth', 'mini_panel.html')

    def post(self, request):
        # form_class = forms.CoinCheckOutForm(requests.POST)

        context = {
            # 'converter_form': form_class,
            'today': Todays_Date,
        }

        return render(request, self.template_name, context)

    def get(self, request):
        # form_class = forms.CoinCheckOutForm()

        context = {
            # 'converter_form': form_class,
            'today': Todays_Date,
        }

        context['malaria_patients'] = malaria_patients
        context['ebola_patients'] = ebola_patients
        context['female_users'] = female_users
        context['male_users'] = male_users
        context['all_users'] = all_users
        context['previous'] = previous

        return render(request, self.template_name, context)


class MedicalInfoForm(custom_views.View):
    template_name = join_path(
        'UserHealth', 'medical_info_form.html')

    def post(self, request):
        form_class = forms.UserHealthInfoForm(request.POST)

        context = {
            'health_form': form_class,
            'today': Todays_Date,
        }

        if form_class.is_valid():
            try:
                form_class.save(request)
            except Exception as Error:
                raise Error

            # reverse('mini-panel')
            return render(request, join_path('UserHealth', 'health_update_success.html'), context)

        return render(request, self.template_name, context)

    def get(self, request):
        form_class = forms.UserHealthInfoForm()

        context = {
            'health_form': form_class,
            'today': Todays_Date,
        }

        return render(request, self.template_name, context)


class MedicalInfoList(custom_views.View):
    template_name = join_path(
        'UserHealth', 'medical_info_list.html')

    def post(self, request):
        # form_class = forms.CoinCheckOutForm(requests.POST)

        context = {
            # 'converter_form': form_class,
            'today': Todays_Date,
        }

        return render(request, self.template_name, context)

    def get(self, request):
        # form_class = forms.CoinCheckOutForm()

        context = {
            # 'converter_form': form_class,
            'today': Todays_Date,
        }

        context['all_user_data'] = all_user_data

        return render(request, self.template_name, context)


class DoctorsView(custom_views.View):
    template_name = join_path(
        'UserHealth', 'doctors.html')

    def post(self, request):

        context = {
            'today': Todays_Date,
        }

        return render(request, self.template_name, context)

    def get(self, request):

        context = {
            'today': Todays_Date,
        }

        return render(request, self.template_name, context)


class EHealthHome(custom_views.View):
    template_name = join_path(
        'UserHealth', 'home.html')

    def post(self, request):

        context = {
            'today': Todays_Date,
        }

        return render(request, self.template_name, context)

    def get(self, request):

        context = {
            'today': Todays_Date,
        }

        return render(request, self.template_name, context)
