# coding:utf-8

from django.views.generic import View
from django.shortcuts import reverse
from django.http import JsonResponse
from app.model.comment import Comment
from app.model.auth import ClientUser
from app.model.video import Video


class CommentView(View):

    def post(self, request):
        content = request.POST.get('content', '')
        user_id = request.POST.get('userId', '')
        video_id = request.POST.get('videoId', '')
        print(content, user_id, video_id)
        if not all([content, user_id, video_id]):
            return JsonResponse({'code': -1, 'msg': '缺少必要字段'})

        video = Video.objects.get(pk=video_id)
        user = ClientUser.objects.get(pk=user_id)
        comment = Comment.objects.create(content=content, user=user, video=video)
        data = {'comment': comment.data()}
        print(data)
        return JsonResponse({'code': 0, 'msg': 'success', 'data': data})



