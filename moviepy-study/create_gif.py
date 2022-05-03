# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/3 0:48
Author: Lison Song
"""
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *  # ImageClip
from datetime import datetime

source_path = os.path.join(SAMPLE_INPUTS, 'video1.mp4')

GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")
os.makedirs(GIF_DIR, exist_ok=True)
'''
my_clip = VideoFileClip("some_file.mp4")
my_clip.set_start(t=5) #没有做任何改变，修改会丢失
my_new_clip = my_clip.set_start(t=5) #这样才对。moviepy中，修改过的clip要重新赋值给变量，修改才会被保存
'''


def create_gif(video_path, gif_path, startT=0, endT=5, is_resize=True, size_width=720, size_height=405, fps=5):
    starttime = datetime.now()
    clip = VideoFileClip(video_path)
    subclip = clip.subclip(startT, endT)
    if is_resize:
        subclip = subclip.resize(width=size_width, height=size_height)
    subclip.write_gif(gif_path, fps=fps, program='ffmpeg')
    endtime = datetime.now()
    print(f"Program create_gif takes {(endtime - starttime).seconds} seconds to run ")


'''
## 指定焦点 位置 生成 gif 
w, h = clip.size
subclip2 = clip.subclip(10, 20)
square_cropped_clip = crop(subclip2, width=320, height=320, x_center=w/2, y_center=h/2)

square_cropped_clip.write_gif(output_path2, fps=fps, program='ffmpeg')
'''
if __name__ == '__main__':
    gif_file = os.path.join(GIF_DIR, 'simple4.gif')
    create_gif(source_path, gif_file)
