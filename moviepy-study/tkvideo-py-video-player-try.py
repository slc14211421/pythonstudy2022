# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/3 11:13
Author: Lison Song
"""
'''
 测试时间： 2022-05-03 11:30
 测试结果： 播放特别慢 原因未知 没时间去仔细研究这个 库，后面空闲的再说
   
 
'''
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from tkinter import *
from tkvideo import tkvideo




if __name__ == '__main__':
    source_path = os.path.join(SAMPLE_INPUTS, 'video1.mp4')
    #create instance for window
    root = Tk()
    #set window title
    root.title('VIDEO PLAYER')
    #create lable
    my_label = Label(root)
    my_label.pack()

    # clip = VideoFileClip(source_path)

    player = tkvideo(source_path, my_label, loop=1, size=(1280, 720))
    player.play()

    root.mainloop()

