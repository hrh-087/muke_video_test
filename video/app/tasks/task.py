# coding:utf-8
import os
import django
import time

django.setup()

from celery.task import task

from app.libs.base_qiniu import video_qiniu
from app.model.video import Video, VideoSub


@task
def video_task(command, out_path, path_name,
               video_file_name, video_sub_id):
    from app.utils.common import remove_path

    # print('##' * 50)
    # print(command, out_path, path_name, video_file_name, number)

    os.system(command)
    out_name = '.'.join([out_path, 'mp4'])

    print(11111111111, out_name, path_name)
    if not os.path.exists(out_name):
        remove_path([out_name, path_name])
        return False

    final_name = '{}_{}'.format(int(time.time()), video_file_name)
    url = video_qiniu.put(final_name, out_name)

    if url:
        try:
            video_sub = VideoSub.objects.get(pk=video_sub_id)
            video_sub.url = url
            video_sub.save()
            return True
        except:
            return False
        finally:
            remove_path([out_name, path_name])
    remove_path([out_name, path_name])
