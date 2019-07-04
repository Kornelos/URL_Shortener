from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.get_link, name=''),
    re_path(r'[A-Za-z0-9]$', views.redirect_link, name='redirect'),
]