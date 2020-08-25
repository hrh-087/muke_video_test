# coding:utf-8

import os
import time
import shutil

from django.conf import settings


def check_and_get_video_type(type_obj, type_value, message):
    try:
        type_obj(type_value)

    except:
        return {'code': -1, 'msg': message}

    return {'code': 0, 'msg': 'success'}


def handle_video(video_file, video_id, number):
    in_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp')
    out_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp_out')
    name = '{}_{}'.format(int(time.time()), video_file.name)
    path_name = '/'.join([in_path,name])
    with open(path_name, 'wb') as f:
        # 3.获取上传文件的内容并写到创建的文件中
        for content in video_file.chunks():   # pic.chunks() 上传文件的内容。
            f.write(content)
    out_name = f'{int(time.time())}_{video_file.name.split(".")[0]}'
    out_path = '/'.join([out_path,out_name])
    command = f'ffmpeg -i {path_name} -c copy {out_path}.mp4'
    os.system(command)
    # print(command)
    return True
#qfm7wmc17.hn-bkt.clouddn.com
