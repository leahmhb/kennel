# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from organizer import views

app_name = 'organizer'
urlpatterns = [
    path('people/', views.PersonList.as_view(), name="people"),
    path('person/detail/<str:slug>/',
         views.PersonDetail.as_view(), name="detail-person"),
    path('person/update/<str:slug>/',
         views.PersonUpdate.as_view(), name="update-person"),


    path('kennels/', views.KennelList.as_view(), name="kennels"),
    path('kennel/detail/<str:slug>/',
         views.KennelDetail.as_view(), name="detail-kennel"),
    path('kennel/update/<str:slug>/',
         views.KennelUpdate.as_view(), name="update-kennel"),
]
