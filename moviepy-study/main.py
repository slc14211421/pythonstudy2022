# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/2 23:13
Author: Lison Song
"""
from moviepy.editor import *

if __name__ == '__main__':
    ## 检查 TextClip 可以用的字体
    print("hellow")
    textclip = TextClip('lison')
    print(textclip.list('color'))
    print(textclip.list('font'))