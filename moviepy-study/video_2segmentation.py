# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/3 2:41
Author: Lison Song
"""
import os
from conf import DATA_INPUTS, DATA_OUTPUTS
from moviepy.editor import *  # ImageClip
from proglog import ProgressBarLogger
from math import floor

def video_2segment(source_video, save_path, startT, endT, taskid=None):

    '''
    很多方法都接受时间参数，clip.subclip(tstart,tend)，截取两个时间点之间的 clip 片段，在这个方法中，时间既可以用(tstart=230.54),以秒的时间来表示，
    也可以用(tstart=(3,50.54))，以 3 分 50.54 秒的形式来表示，还可以 (tstart=(0,3,50.54))或者 (tstart=(00:03:50.54)),以，小时，分钟，秒的形式老表示。
    大多数没有赋值的时间参数会有一个默认值，比如 clip.subclip(tstart=50)，tend 的默认值就是视频的长度，clip.subclip(tend=50)，那么 tstart 就默认为 0.
    当时间是负数的时候，代表倒数 n 秒。比如，clip.subclip(-20, -10)会截取倒数 20 秒到倒数 10 秒之间的片段。
    视频切片程序
    暂时省略 参数验证部分
    :param source_video:
    :param save_path:
    :param startT:
    :param endT:
    :return:
    '''
    my_logger = MyBarLogger(taskid)
    clip = VideoFileClip(source_video)
    duration = int(clip.duration)
    if startT >= endT:
        return False
    if endT > duration:
        endT = duration
    subclip = clip.subclip(startT, endT)
    subclip.write_videofile(save_path, codec='libx264', audio_codec="aac",  logger=my_logger)
    return True


def callback(message):
    print(message)

class MyBarLogger(ProgressBarLogger):
    def __init__(self, tsakid):
        super().__init__(init_state=None, bars=None, ignored_bars=None,
                 logged_bars='all', min_time_interval=0, ignore_bars_under=0)
        self.taskid = tsakid
    def callback(self, **changes):
        # Every time the logger is updated, this function is called with
        # the `changes` dictionnary of the form `parameter: new value`.
        # the `try` is to avoid KeyErrors before moviepy generates a `'t'` dict
        try:
            # print(self.state)
            index = self.state['bars']['t']['index']
            total = self.state['bars']['t']['total']
            percent_complete = index / total * 100
            if percent_complete < 0:
                percent_complete = 0
            if percent_complete > 100:
                percent_complete = 100
            # if floor(percent_complete) % 10 == 0:
            #     ## call http post api
            #     print(f"task {self.taskid} : {index} of {total} video frames complete... ({floor(percent_complete)}%)")
            print(f"task {self.taskid} : {index} of {total} video frames complete... ({floor(percent_complete)}%)")
        except KeyError as e:
            pass


if __name__ == '__main__':
    source_video = os.path.join(DATA_INPUTS, 'video1.mp4')
    # video_2segment(source_video, os.path.join(DATA_OUTPUTS, 'segment1.mp4'), startT=0, endT=5)
    video_2segment(source_video, os.path.join(DATA_OUTPUTS, 'segment2.mp4'), startT=6, endT=10, taskid='CHS1000001')
    # video_2segment(source_video, os.path.join(DATA_OUTPUTS, 'segment3.mp4'), startT=11, endT=15)
    # video_2segment(source_video, os.path.join(DATA_OUTPUTS, 'segment4.mp4'), startT=16, endT=20)
