# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import path, include, re_path

from poodles import views

app_name = 'poodles'
urlpatterns = [
	path('', views.PoodleIndexView.as_view(), name='index'),
    path('poodle-list/', views.PoodleListView.as_view(), name="list"),
    path('poodle/<int:id>/', views.PoodleUpdateView.as_view(), name="update"),
]
