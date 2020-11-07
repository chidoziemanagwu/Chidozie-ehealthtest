from django import forms
from .models import UserProfile
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

JOB_DESCRIPTIONS = (

    ("", "Doctor"),
    ("NUR", "Nurologist"),
    ("Bae_D", "Baby Doc"),
    ("P_D", "Pregnancy Doc"),
    ("Bon_D", "Bone Doc"),
    ("P_S", "Plastic Surgeon"),
)


HealthUserModel = get_user_model()


class RegisterationForm(UserCreationForm):

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'firstNameField',
                'name': 'firstname',
                'placeholder': 'First Name',
                'class': 'form-control bg-white border-left-0 border-md',

            }
        )
    )

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'lastNameField',
                'name': 'lastname',
                'placeholder': 'Last Name',
                'class': 'form-control bg-white border-left-0 border-md',
            }
        )
    )

    username = forms.CharField(
        label='User Name',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'usernameField',
                'name': 'username',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'User Name',
            }
        )
    )

    email = forms.CharField(
        label='Email Address',
        widget=forms.EmailInput(
            attrs={

                'type': 'email',
                'id': 'useremailField',
                'name': 'useremail',
                'placeholder': 'Email',
                'class': 'form-control bg-white border-left-0 border-md',

            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={

                'type': 'password',
                'name': 'password',
                'id': 'passwordField',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Password',

            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={

                'type': 'password',
                'class': 'form-control bg-white border-left-0 border-md',
                'name': 'confirm-password',
                'id': 'confirmPasswordField',
                'placeholder': 'Confirm Password',

            }
        )
    )

    class Meta:
        model = HealthUserModel
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2',
                  )

        # exclude = ('first_name',
        #            'last_name',
        #            )

    def clean_email(self):
        useremail = self.cleaned_data['email'].lower()
        Auth_user = HealthUserModel.objects.filter(email=useremail)
        if Auth_user.exists():
            raise ValidationError(
                f'This user email: "{useremail}" is already in use !!')
        return useremail

    def save(self, commit=True):
        Auth_user = super(RegisterationForm, self).save(commit=False)
        Auth_user.username = self.cleaned_data['username']
        Auth_user.email = self.cleaned_data['email']

        if commit:
            Auth_user.save()

        return Auth_user


class UserProfileForm(forms.ModelForm):
    ''' NOTE!!!: Do not touch this class for an reason. The text input types are there because
    postgres db has a problem with normal integer field, I don't know why. '''

    userphonenumber = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'userphone',
                'maxlength': '20',
                'name': 'phonenumber',
                'class': 'form-control bg-white border-md border-left-0 pl-3',
                'placeholder': 'Phone Number',
            }
        )
    )

    # job_title = forms.ChoiceField(
    #     choices=JOB_DESCRIPTIONS,
    #     widget=forms.Select(
    #         attrs={

    #             'id': 'jobTitleField',
    #             'placeholder': 'Choose job description',
    #             'class': 'form-control custom-select bg-white border-left-0 border-md',
    #             # 'data-dropdown-css-class':'woox--select-squared-dropdown-dark',

    #         }
    #     )
    # )

    medical_practitioner = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={

                # 'class': 'onoffswitch',
                # 'style': 'display:none;',
                'id': 'medicalPractioner',
            }
        )
    )

    class Meta:
        model = UserProfile
        fields = ('userphonenumber',
                  'medical_practitioner',
                  'job_title',
                  )

    # You must use the exact name of the field in the form here or the function wont't run.
    def clean_userphonenumber(self):
        phonenumber = self.cleaned_data['userphonenumber']
        Auth_user = UserProfile.objects.filter(
            userphonenumber=phonenumber
        )
        try:
            if int(phonenumber) and not str(phonenumber):
                min_length = 10
                max_length = 13
                ph_length = str(phonenumber)
                if len(ph_length) < min_length or len(ph_length) > max_length:
                    raise ValidationError('Phone number length not valid')

            if Auth_user.exists():
                raise ValidationError(
                    f'This user phone number: "{phonenumber}" is already in use !!')

        except (ValueError, TypeError):
            raise ValidationError('Please enter a valid phone number')

        return phonenumber

    def save(self, commit=True):
        UserProfile = super(UserProfileForm, self).save(commit=False)
        try:
            UserProfile.userphonenumber = self.cleaned_data['userphonenumber']
            UserProfile.job_title = self.cleaned_data['job_title']
            UserProfile.medical_practitioner = self.cleaned_data['medical_practitioner']
        except Exception as Error:
            raise (Error)

        if commit:
            try:
                UserProfile.save()
            except Exception as Error:
                raise (Error)

        return UserProfile


class DoctorProfileForm(forms.ModelForm):
    ''' NOTE!!!: Do not touch this class for an reason. The text input types are there because
    postgres db has a problem with normal integer field, I don't know why. '''

    userphonenumber = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'userphone',
                'maxlength': '20',
                'name': 'phonenumber',
                'class': 'form-control bg-white border-md border-left-0 pl-3',
                'placeholder': 'Phone Number',
            }
        )
    )

    job_title = forms.CharField(
        label='Job Title',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'jobtitle',
                'maxlength': '25',
                'name': 'jobtitle',
                'class': 'form-control bg-white border-md border-left-0 pl-3',
                'placeholder': 'Job Description',
            }
        )
    )

    # job_title = forms.ChoiceField(
    #     choices=JOB_DESCRIPTIONS,
    #     widget=forms.Select(
    #         attrs={

    #             'id': 'jobTitleField',
    #             'placeholder': 'Choose job description',
    #             'class': 'form-control custom-select bg-white border-left-0 border-md',
    #             # 'data-dropdown-css-class':'woox--select-squared-dropdown-dark',

    #         }
    #     )
    # )

    medical_practitioner = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={

                # 'class': 'onoffswitch',
                # 'style': 'display:none;',
                'id': 'medicalPractioner',
                'checked': 'checked',
            }
        )
    )

    class Meta:
        model = UserProfile
        fields = ('userphonenumber',
                  'medical_practitioner',
                  'job_title',
                  )

    # You must use the exact name of the field in the form here or the function wont't run.
    def clean_userphonenumber(self):
        phonenumber = self.cleaned_data['userphonenumber']
        Auth_user = UserProfile.objects.filter(
            userphonenumber=phonenumber
        )
        try:
            if int(phonenumber) and not str(phonenumber):
                min_length = 10
                max_length = 13
                ph_length = str(phonenumber)
                if len(ph_length) < min_length or len(ph_length) > max_length:
                    raise ValidationError('Phone number length not valid')

            if Auth_user.exists():
                raise ValidationError(
                    f'This user phone number: "{phonenumber}" is already in use !!')

        except (ValueError, TypeError):
            raise ValidationError('Please enter a valid phone number')

        return phonenumber

    def save(self, commit=True):
        UserProfile = super(DoctorProfileForm, self).save(commit=False)
        try:
            UserProfile.userphonenumber = self.cleaned_data['userphonenumber']
            UserProfile.job_title = self.cleaned_data['job_title']
            UserProfile.medical_practitioner = self.cleaned_data['medical_practitioner']
        except Exception as Error:
            raise (Error)

        if commit:
            try:
                UserProfile.save()
            except Exception as Error:
                raise (Error)

        return UserProfile


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'name': 'username',
                'class': 'form-control bg-white border-md border-left-0 pl-3',
                'placeholder': 'Username',
                'id': 'loginUsernameField',
            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={

                'type': 'password',
                'name': 'password',
                'id': 'passwordField',
                'class': 'form-control bg-white border-md border-left-0 pl-3',
                'placeholder': 'Password',
            }
        )
    )

    remember_me = forms.BooleanField(
        required=False,
        label='Remember Me',
        widget=forms.CheckboxInput(
            attrs={

                'type': 'checkbox',
                'name': 'CheckboxInput',
                'id': 'customCheckLogin',
                'placeholder': 'Password',
                'class': 'custom-control-input',
            }
        )
    )

    class Meta:
        model = HealthUserModel

        fields = (
            'username',
            'email',
            'password',
        )

        exclude = ('first_name',
                   'last_name',
                   )
