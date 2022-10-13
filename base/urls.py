from django.contrib import admin
from unicodedata import name
from django.urls import path 
from . import views
from django.http import HttpResponse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('submitform/', views.form_submit,  name='Submitform'),
]

