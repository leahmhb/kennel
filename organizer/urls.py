# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from organizer import views

app_name = 'organizer'
urlpatterns = [
    path('people/', views.PersonList.as_view(), name="all-people"),
    path('person/<str:slug>/', views.PersonDetail.as_view(), name="one-person"),
    path('kennels/', views.KennelList.as_view(), name="all-kennels"),
    path('kennel/<str:slug>/', views.KennelDetail.as_view(), name="one-kennel"),
]
