from django.contrib import admin
from django.urls import path
from lessonFieldsTypeAPP import views

urlpatterns = [
    path('',views.index),
    path('news', views.news),

]
