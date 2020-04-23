# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from poodles import views

app_name = 'poodles'
urlpatterns = [
    path('', views.PoodleIndex.as_view(), name='home'),
    path('poodles/', views.PoodleList.as_view(), name="poodles"),
    path('poodle/new/',
         views.PoodleNew.as_view(), name="new"),
    path('poodle/detail/<str:slug>/',
         views.PoodleDetail.as_view(), name="detail"),
    path('poodle/update/<str:slug>/',
         views.PoodleUpdate.as_view(), name="update"),
    path('poodle/create/<str:slug>/',
         views.PoodleUpdate.as_view(), name="create"),
    path('poodle/delete/<str:slug>/',
         views.PoodleUpdate.as_view(), name="delete"),


    path('poodle/document/new/<str:slug>/',
         views.DocumentNew.as_view(), name="document-new"),
    path('poodle/document/update/<str:slug>/',
         views.DocumentUpdate.as_view(), name="document-update"),
    path('poodle/image/new/<str:slug>/',
         views.ImageNew.as_view(), name="image-new"),
    path('poodle/image/update/<str:slug>/',
         views.ImageUpdate.as_view(), name="image-update"),
]
