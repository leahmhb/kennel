# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import path, include, re_path

from poodles.views import PoodleIndex, PoodleList, PoodleDetail

app_name = 'poodles'
urlpatterns = [
    path('', PoodleIndex.as_view(), name='index'),
    path('poodle-list/', PoodleList.as_view(), name="list"),
    path('poodle/<str:akc>/', PoodleDetail.as_view(), name="detail"),
]
