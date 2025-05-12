# user_management/urls.py
from django.urls import path
from .views import update_profile

urlpatterns = [
    path('profile', update_profile, name='update_profile'),
]
