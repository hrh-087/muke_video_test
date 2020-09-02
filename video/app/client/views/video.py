# coding:utf-8

from django.views.generic import View
from django.shortcuts import redirect, reverse, get_object_or_404

from app.libs.base_render import render_to_response
from app.model.video import Video, FromType


class ExVideo(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.exclude(from_to=FromType.custom.value)

        data = {'videos': videos}

        return render_to_response(request, self.TEMPLATE, data)


class VideoSubView(View):
    TEMPLATE = 'client/video/videosub.html'

    def get(self, request, video_id):
        video = get_object_or_404(Video, pk=video_id)
        data = {'video': video}

        return render_to_response(request, self.TEMPLATE, data=data)
