# coding:utf-8

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from app.dashboard import urls as dashboard_urls
from app.client import urls as client_urls

print(dashboard_urls)
urlpatterns = [
    path('dashboard/', include(dashboard_urls)),
    path('client/', include(client_urls)),
]
urlpatterns += staticfiles_urlpatterns()