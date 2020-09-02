# coding:utf-8

from django.urls import path
from .views.base import Index
from .views.video import ExVideo, VideoSubView

urlpatterns = [
    path('', Index.as_view(), name='client_index'),
    path('video/ex', ExVideo.as_view(), name='client_ex_video'),
    path('video/<int:video_id>', VideoSubView.as_view(), name='client_video_sub'),
]
