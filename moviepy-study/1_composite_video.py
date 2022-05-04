# -*- coding: utf-8 -*-
# @Author  : Lison Song
# @Time    : 2022/5/4 10:07

# import gizeh
# import moviepy.editor as mpy
from conf import DATA_INPUTS, DATA_OUTPUTS
from os import path, makedirs
from moviepy.editor import *

'''
OSError: no library called "cairo-2" was found
no library called "cairo" was found

cairo-2 windows 环境配置异常 后面有时间的话 再测试吧
'''


# def make_frame(t):
#     surface = gizeh.Surface(width=320, height=260)  # 宽、高
#     radius = surface.width * (1 + (t * (2 - t)) ** 2) / 6  # 半径随时间变化
#     circle = gizeh.circle(radius, xy=(64, 64), fill=(1, 0, 0))
#     circle.draw(surface)
#     return surface.getnpimage()  # 返回一个8bit RGB数组


def mixing_1(sourcelist):
    '''
    简单地把多个视频合成到一起的两种最简单的办法。1.把视频一个接一个地拼接起来。2.视频叠加在一块，比如一个大的画面同时播几个视频。
    视频拼接我们使用 concatenate_videoclips 函数来完成。
    注意-1：视频合并前 必须将分辨率调整一致 否则会很奇怪
    :param sourcelist: 待合并的视频文件list
    :return:
    '''

    clips = []
    for vidfile in sourcelist:
        clip = VideoFileClip(vidfile).resize(width=1280, height=720)
        clips.append(clip)

    finalclip = concatenate_videoclips(clips)
    finalclip.write_videofile(path.join(DATA_OUTPUTS, "mixing_1.mp4"), fps=25, codec='libx264', bitrate='2000k',
                              audio_codec="aac", audio_bitrate='128k')


def mixing_2(source):
    '''
    合并成9宫格效果的视频
    finalclip 会按照 clip1，clip2，clip3 的顺序将这三个 clip 播放。这些 clip 并不需要相同的时长或者大小，仅仅是首尾相连而已。我们还可以通过 transition=my_clip
    这个参数来设置一下 clip 之间衔接的过渡动画。视频叠加我们使用 clip_array 函数来完成
    :param source:
    :return:
    '''
    clip1 = VideoFileClip(source).margin(10)
    clip2 = clip1.fx(vfx.mirror_x)  # x轴镜像
    clip3 = clip1.fx(vfx.mirror_y)  # y轴镜像
    clip4 = clip1.resize(0.6)  # 尺寸等比缩放0.6
    final_clip = clips_array([
        [clip1, clip2],
        [clip3, clip4]
    ])
    final_clip.resize(width=1280, height=720).write_videofile(path.join(DATA_OUTPUTS, "mixing_2.mp4"), fps=25,
                                                              codec='libx264', bitrate='2000k', audio_codec="aac",
                                                              audio_bitrate='128k')


if __name__ == '__main__':
    GIF_DIR = path.join(DATA_OUTPUTS, 'gifs')
    makedirs(GIF_DIR, exist_ok=True)

    # clip = mpy.VideoClip(make_frame, duration=2)
    # clip.write_gif(path.join(GIF_DIR, 'circle.gif'), fps=15)

    ## 视屏合并测试1 简单 拼合
    vidfiles_list =[path.join(DATA_INPUTS, 'video4.mp4'), path.join(DATA_INPUTS, 'video5.mp4'), path.join(DATA_INPUTS, 'video6.mp4')]
    mixing_1(vidfiles_list)

    ## 视屏合并测试2 视频翻转拼合 简单的 9宫格效果
    # mixing_2(path.join(DATA_INPUTS, 'video5.mp4'))
