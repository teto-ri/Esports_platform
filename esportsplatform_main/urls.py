from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('competition_registration', views.competition_registration, name='competition_registration'),
]