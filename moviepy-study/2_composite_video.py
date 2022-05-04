# -*- coding: utf-8 -*-
# @Author  : Lison Song
# @Time    : 2022/5/4 10:07

# import gizeh
# import moviepy.editor as mpy
from conf import DATA_INPUTS, DATA_OUTPUTS
from os import path, makedirs
from moviepy.editor import *




def mixing_3(sourcelist):
    '''
    CompositeVideoClip 这个类提供来更加灵活的方式来排版视频，但是它可要比 concatenate_videoclips 和 clips_array 要复杂的多了。
    开始和结束时间: 在堆叠视频中，每个 clip 会在通过 clip.start(5) 函数声明的时间开始播放，我们可以像下面这样去设置。
    Positioning clips: clip 们的位置设定。
    video = CompositeVideoClip([
                            clip1,
                            clip2.set_pos((45,150)),
                            clip3.set_pos((90,100))
                            ])
    clip2.set_pos((45,150)) #像素坐标
    clip2.set_pos("center") #居中
    clip2.set_pos(("center","top")) #水平方向居中，但是处置方向放置在顶部
    clip2.set_pos(("left","center")) #水平方向放置在左边，垂直方向居中
    clip2.set_pos((0.4,0.7), relative=True) #0.4倍宽，0.7倍高处
    clip2.set_pos(lambda t: ('center', 50+t)) #水平居中，向下移动

    Compositing audio clips:合成声音 clips
    如果你有一些特殊的的定制合成音频的需求，应该使用 CompositeAudioClip 和 concatenate_audioclips 这俩类。
    concat = concatenate_audioclips([clip1, clip2, clip3])
    compo = CompositeAudioClip([
                            aclip1.volumex(1.2),
                            aclip2.set_start(5), # start at t=5s
                            aclip3.set_start(9)
                            ])
    :param sourcelist: 待合并的视频文件list
    :return:
    '''
    clip1 = VideoFileClip(sourcelist[0]).resize(width=1280, height=720)
    clip2 = VideoFileClip(sourcelist[1]).resize(width=1280, height=720)
    clip3 = VideoFileClip(sourcelist[2]).resize(width=1280, height=720)
    finalclip = CompositeVideoClip([
        clip1,
        clip2.set_start(5).crossfadein(1),
        clip3.set_start(9).crossfadein(1.5)
    ])
    # finalclip.preview(fps=25)
    finalclip.write_videofile(path.join(DATA_OUTPUTS, "mixing_3.mp4"), fps=25, codec='libx264', bitrate='2000k',
                               audio_codec="aac", audio_bitrate='128k')


if __name__ == '__main__':
    ## 视屏合并测试3 CompositeVideoClip 拼合
    vidfiles_list =[path.join(DATA_INPUTS, 'video4.mp4'), path.join(DATA_INPUTS, 'video5.mp4'), path.join(DATA_INPUTS, 'video6.mp4')]
    mixing_3(vidfiles_list)



