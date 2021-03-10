# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.articles_list , name="list"),
    path('<article_details>', views.articles_detail , name="detail"),

]
