# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from choices import views

app_name = 'choices'
urlpatterns = [
    path('states/', views.get_states, name='get-states'),
    path('countries/', views.get_countries, name='get-countries'),
    path('sexes/', views.get_sexes, name='get-sexes'),
    path('colors/', views.get_colors, name='get-colors'),
]
