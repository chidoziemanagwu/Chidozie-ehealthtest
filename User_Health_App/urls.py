from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('',
         views.EHealthHome.as_view(),
         name='eHealth-home'),

    path('doctors/',
         login_required(views.DoctorsView.as_view()),
         name='doctors'),

    path('mini-panel/',
         login_required(views.MiniPanelView.as_view()),
         name='mini-panel'),
    
    path('medical-info-form/',
         login_required(views.MedicalInfoForm.as_view()),
         name='medical-info-form'),

    path('medical-info-list/',
         login_required(views.MedicalInfoList.as_view()),
         name='medical-info-list'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
