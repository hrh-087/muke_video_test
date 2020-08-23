# coding:utf-8

from django.views.generic import View
from django.shortcuts import redirect, reverse
from app.libs.base_render import render_to_response
from app.utils.permission import dashboard_auth
from app.model.video import (Video, VideoStar, VideoSub,
                             VideoType, FromType,
                             IdentityType,
                             NationalityType)
from app.utils.common import check_and_get_video_type


class ExternaVideo(View):
    TEMPLATE = 'dashboard/video/externa_video.html'

    @dashboard_auth
    def get(self, request):
        error = request.GET.get('error', '')
        data = {'error': error}

        video = Video.objects.exclude(from_to=FromType.custom.value)
        data['videos'] = video
        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):
        name = request.POST.get('name')
        image = request.POST.get('image')
        video_type = request.POST.get('video_type')
        from_to = request.POST.get('from_to')
        nationality = request.POST.get('nationality')
        description = request.POST.get('info')

        print(name, image, video_type, from_to, nationality, description)
        if not all([name, image, video_type, from_to, nationality, description]):
            return redirect('{}?error={}'.format(
                reverse('video_externa'), '缺少必要字段'))

        result = check_and_get_video_type(
            VideoType, video_type, '非法的视频类型')

        if result.get('code') != 0:
            return redirect('{}?error={}'.format(
                reverse('video_externa'), result.get('msg')))

        result = check_and_get_video_type(
            FromType, from_to, '非法的来源')

        if result.get('code') != 0:
            return redirect('{}?error={}'.format(
                reverse('video_externa'), result.get('msg')))

        result = check_and_get_video_type(
            NationalityType, nationality, '非法的国籍')

        if result.get('code') != 0:
            return redirect('{}?error={}'.format(
                reverse('video_externa'), result.get('msg')))

        Video.objects.create(
            name=name,
            image=image,
            video_type=video_type,
            from_to=from_to,
            nationality=nationality,
            info=description)

        return redirect(reverse('video_externa'))


class VideoSubView(View):
    TEMPLATE = 'dashboard/video/video_sub.html'

    @dashboard_auth
    def get(self, request, video_id):
        data = {}
        video = Video.objects.get(pk=video_id)
        error = request.GET.get('error', '')

        data['error'] = error
        data['video'] = video
        return render_to_response(request, self.TEMPLATE, data)

    def post(self, request, video_id):
        url = request.POST.get('url')
        print(url, video_id)
        video = Video.objects.get(pk=video_id)

        length = video.video_sub.count()
        pash_format = '{}'.format(reverse('video_sub', kwargs={'video_id': video_id}))
        try:
            VideoSub.objects.create(video=video, url=url, number=length + 1)
        except:
            return redirect('{}?error{}'.format(pash_format, '创建失败'))

        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))


class VideoStarView(View):

    def post(self, request):
        name = request.POST.get('name')
        identity = request.POST.get('identity')
        video_id = request.POST.get('video_id')

        pash_format = '{}'.format(reverse('video_sub', kwargs={'video_id': video_id}))

        if not all([name, identity, video_id]):
            return redirect('{}?error{}'.format(pash_format, '缺少必要字段'))

        result = check_and_get_video_type(
            IdentityType, identity, '非法的身份')

        if result.get('code') != 0:
            return redirect('{}?error={}'.format(pash_format, result['msg']))

        video = Video.objects.get(pk=video_id)
        try:
            VideoStar.objects.create(
                video=video,
                name=name,
                identity=identity
            )
        except:
            return redirect('{}?error={}'.format(pash_format, '创建失败'))
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))


class StarDelete(View):

    def get(self, request, star_id, video_id):
        VideoStar.objects.filter(id=star_id).delete()
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))
