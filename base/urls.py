from django.contrib import admin
from unicodedata import name
from django.urls import path 
from . import views
from django.http import HttpResponse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name="landing"),
    path('multiple/', views.multiple, name="multiple"),
    path('single/', views.single, name="single"),
    path('submitform/', views.form_submit,  name='Submitform'),
    path('submitformsingle/', views.single_form, name='Singleform'),
    # path('tictactoe/', views.tictac, name="tictactoegame"),
    # path('wordle/', views.wordle, name="wordlegame"),
]

