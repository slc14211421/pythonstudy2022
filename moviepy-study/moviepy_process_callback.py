# -*- coding: utf-8 -*-
# @Author  : Lison Song
# @Time    : 2022/5/3 22:46
from proglog import ProgressBarLogger
from math import floor

class MyBarLogger(ProgressBarLogger):
    '''
    USE e.g:
    mylog=MyBarLogger("CHS-GIF-T00000001")
    subclip.write_gif(gif_path, fps=fps, program='ffmpeg', logger=mylog)
    '''
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
