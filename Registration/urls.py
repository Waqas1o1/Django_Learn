from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Registration,name='RegistrationPage'),
    path('registration/',views.HandleRegistration,name='RegistrationPage'),
]
