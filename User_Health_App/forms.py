from .models import *
from django import forms
from django.conf import settings
from os.path import join as join_path

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserHealthInfoForm(forms.ModelForm):

    Gender = forms.CharField(
        # label='Your gender',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'gender',
                'name': 'gender',
                'class': 'form-control bg-white border-md pl-3',
                'placeholder': 'Your gender',
            }
        )
    )

    age = forms.CharField(
        # label='Your age',
        widget=forms.EmailInput(
            attrs={

                'type': 'text',
                'id': 'age',
                'name': 'age',
                'class': 'form-control bg-white border-md pl-3',
                'placeholder': 'Your age',
            }
        )
    )

    blood_group = forms.CharField(
        # label='Your blood group',
        widget=forms.TextInput(
            attrs={

                'id': 'blood-group',
                'name': 'blood-group',
                'class': 'form-control bg-white border-md pl-3',
                'placeholder': 'Your blood group',
            }
        )
    )

    genotype = forms.CharField(
        # label='Your genotype',
        widget=forms.TextInput(
            attrs={

                'id': 'genotype',
                'name': 'genotype',
                'class': 'form-control bg-white border-md pl-3',
                'placeholder': 'Your genotype',
            }
        )
    )

    ebola_status = forms.BooleanField(
        required=False,
        label='Do you have ebola currently?',
        widget=forms.CheckboxInput(
            attrs={

                'class': 'm-2',
                'id': 'ebolaStatus',
                # 'checked': 'checked',
            }
        )
    )

    malaria_status = forms.BooleanField(
        required=False,
        label='Do you have malaria currently?',
        widget=forms.CheckboxInput(
            attrs={

                'class': 'm-2',
                'id': 'malariaStatus',
                # 'checked': 'checked',
            }
        )
    )

    previous = forms.BooleanField(
        required=False,
        label='Do you have any previous health challenges?',
        widget=forms.CheckboxInput(
            attrs={

                'class': 'm-2',
                'id': 'previousHealthIssues',
                # 'checked': 'checked',
                'onclick': 'yesnoCheck()',
            }
        )
    )

    previous_illness1 = forms.CharField(
        required=False,
        label='What was your illness?',
        widget=forms.TextInput(
            attrs={

                'maxlength': '20',
                'style': 'display:none;',
                'id': 'previous-illness1',
                'name': 'previous-illness1',
                'class': 'form-control bg-white border-md pl-3',
                'placeholder': 'What was your illness?',
            }
        )
    )

    previous_illness2 = forms.CharField(
        required=False,
        label='Subject',
        widget=forms.TextInput(
            attrs={

                'style': 'display:none;',
                'id': 'previous-illness2',
                'name': 'previous-illness2',
                'class': 'form-control bg-white border-md pl-3',
                'placeholder': 'What was your illness?',
            }
        )
    )

    previous_illness3 = forms.CharField(
        required=False,
        label='Write your message here',
        widget=forms.TextInput(
            attrs={

                'style': 'display:none;',
                'id': 'previous-illness3',
                'name': 'previous-illness3',
                'class': 'form-control bg-white border-md pl-3',
                'placeholder': 'What was your illness?',
            }
        )
    )

    previous_illness4 = forms.CharField(
        required=False,
        label='Write your message here',
        widget=forms.TextInput(
            attrs={

                'style': 'display:none;',
                'id': 'previous-illness4',
                'name': 'previous-illness4',
                'class': 'form-control bg-white border-md pl-3',
                'placeholder': 'What was your illness?',
            }
        )
    )

    previous_illness5 = forms.CharField(
        required=False,
        label='Write your message here',
        widget=forms.TextInput(
            attrs={

                'style': 'display:none;',
                'id': 'previous-illness5',
                'name': 'previous-illness5',
                'class': 'form-control bg-white border-md pl-3',
                'placeholder': 'What was your illness?',
            }
        )
    )

    class Meta:
        model = UserHealthInfo
        fields = (
            'Gender',
            'age',
            'blood_group',
            'genotype',
            'ebola_status',
            'malaria_status',
            'previous',
            'previous_illness1',
            'previous_illness2',
            'previous_illness3',
            'previous_illness4',
            'previous_illness5',
        )

    def save(self, request, commit=True):
        UserHealthInfo_instance = super(UserHealthInfoForm, self).save(commit=False)
        UserHealthInfo_instance.user = request.user
        UserHealthInfo_instance.Gender = self.cleaned_data['Gender']
        UserHealthInfo_instance.age = self.cleaned_data['age']
        UserHealthInfo_instance.blood_group = self.cleaned_data['blood_group']
        UserHealthInfo_instance.genotype = self.cleaned_data['genotype']
        UserHealthInfo_instance.ebola_status = self.cleaned_data['ebola_status']
        UserHealthInfo_instance.malaria_status = self.cleaned_data['malaria_status']
        UserHealthInfo_instance.previous = self.cleaned_data['previous']
        UserHealthInfo_instance.previous_illness1 = self.cleaned_data['previous_illness1']
        UserHealthInfo_instance.previous_illness2 = self.cleaned_data['previous_illness2']
        UserHealthInfo_instance.previous_illness3 = self.cleaned_data['previous_illness3']
        UserHealthInfo_instance.previous_illness4 = self.cleaned_data['previous_illness4']
        UserHealthInfo_instance.previous_illness5 = self.cleaned_data['previous_illness5']

        # try:
        #     UserHealthInfo_instance.visitorphonenumber = self.cleaned_data['visitorphonenumber']
        # except Exception as Error:
        #     raise (Error)

        if commit:
            try:
                UserHealthInfo_instance.save()
            except Exception as Error:
                raise (Error)

        return UserHealthInfo_instance
