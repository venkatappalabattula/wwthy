from unicodedata import name
from django.urls import path 
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name="home"),
    path('submitform/', views.form_submit,  name='Submitform'),
]