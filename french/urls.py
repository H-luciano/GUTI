# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from .views import French, FrenchList

app_name = 'french'

urlpatterns = [
    url(r'^main_fr/', French.as_view(), name = 'main_fr'),

    url(r'^list_fr/', FrenchList.as_view(), name = 'list_fr'),


]
