# coding:utf-8

from django.views.generic import View
from django.shortcuts import reverse
from django.http import JsonResponse


class Comment(View):

    def post(self, request):
        content = request.POST.get('content', '')
        user_id = request.POST.get('userId', '')
        video_id = request.POST.get('videoId', '')

        if not all([content, user_id, video_id]):
            return JsonResponse({'code': -1, 'msg': '缺少必要字段'})

        print(content, user_id, video_id)

        return JsonResponse({'code': 0, 'msg': 'success'})