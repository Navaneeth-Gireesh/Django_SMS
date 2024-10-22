from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.sample_sms, name ='sample_sms'),
    path('sms_success', views.sms_success, name = 'sms_success')
]
