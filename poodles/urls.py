# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from poodles import views

app_name = 'poodles'
urlpatterns = [
    path('', views.PoodleIndex.as_view(), name='home'),
    path('poodles/', views.PoodleList.as_view(), name="poodles"),
    path('poodle/detail/<str:slug>/',
         views.PoodleDetail.as_view(), name="detail"),
    path('poodle/update/<str:slug>/',
         views.PoodleUpdate.as_view(), name="update"),
    path('poodle/create/<str:slug>/',
         views.PoodleUpdate.as_view(), name="create"),
    path('poodle/delete/<str:slug>/',
         views.PoodleUpdate.as_view(), name="delete"),
]
