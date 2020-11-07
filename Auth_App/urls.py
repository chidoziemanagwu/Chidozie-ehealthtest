from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt, csrf_protect

urlpatterns = [

    path('validate-username',
         csrf_exempt(views.UsernameValidationView.as_view()),
         name="validate-username"),


    path('validate-email',
         csrf_exempt(views.EmailValidationView.as_view()),
         name='validate_email'),

    path('User-sign-up/',
         views.UserRegisterView.as_view(),
         name='user-register'),

    path('Doctor-sign-up/',
         views.DoctorRegisterView.as_view(),
         name='doctor-register'),

    # path('activate/<str:user_id>/<str:token>',
    #      views.ActivateAccountView.as_view(),
    #      name='activate'),

    path('sign-in/',
         views.UserLoginView.as_view(),
         name='login'),

    # path('authentication-error/',
    #      views.AuthenticationError.as_view(),
    #      name='auth-error'),

    path('sign-out/',
         views.UserLogoutView.as_view(),
         name='logout'),

    # path('email-sent/',
    #      views.EmailSent.as_view(),
    #      name='email-sent'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
