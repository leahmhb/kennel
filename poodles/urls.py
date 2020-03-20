# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from poodles import views

app_name = 'poodles'
urlpatterns = [
    path('', views.PoodleIndex.as_view(), name='home'),
    path('poodles/', views.PoodleList.as_view(), name="all"),
    path('poodle/<str:slug>/', views.PoodleDetail.as_view(), name="one"),
]
