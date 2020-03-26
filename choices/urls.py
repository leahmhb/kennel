# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from choices import views

app_name = 'choices'
urlpatterns = [
    path('json/<str:field>', views.get_json, name='json'),

]
