# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from .views import FrenchSetView, FrenchQuestion, FrenchList

urlpatterns = [
    url(r'^main_fr/', FrenchQuestion.as_view(), name = 'main_fr'),
    url(r'^set_fr/', FrenchSetView.as_view(), name = 'set_fr'),
    url(r'^list_fr/', FrenchList.as_view(), name = 'list_fr'),


]
