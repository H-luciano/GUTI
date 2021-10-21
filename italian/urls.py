# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from .views import Italian, ItalianList

app_name = 'italian'

urlpatterns = [
    url(r'^main_it/', Italian.as_view(), name = 'main_it'),

    url(r'^list_it/', ItalianList.as_view(), name = 'list_it'),


]
