# -*- coding: utf-8 -*-
# @Author  : Lison Song
# @Time    : 2022/5/3 23:11
import os.path
from conf import DATA_INPUTS, DATA_OUTPUTS
from moviepy_process_callback import MyBarLogger
from moviepy.editor import *


def transcoder1(source_path, outputfile):
    print(source_path, outputfile)
    taskid = 'Transcoder01-0000001'
    mylog = MyBarLogger(taskid)
    clip = VideoFileClip(source_path)
    print(clip.reader.fps)
    print(clip.reader.duration)
    print(clip.reader.size)
    subclip = clip.resize(width=1280, height=720)
    '''
    write_videofile(self, filename, fps=None, codec=None,
                        bitrate=None, audio=True, audio_fps=44100,
                        preset="medium",
                        audio_nbytes=4, audio_codec=None,
                        audio_bitrate=None, audio_bufsize=2000,
                        temp_audiofile=None,
                        rewrite_audio=True, remove_temp=True,
                        write_logfile=False, verbose=True,
                        threads=None, ffmpeg_params=None,
                        logger='bar'):
    '''
    subclip.write_videofile(outputfile, fps=25, codec='libx264', bitrate='2000k', audio_codec="aac", audio_bitrate='128k', logger=mylog)
    print(f"{taskid} trans over")



if __name__ == '__main__':
    source_path = os.path.join(DATA_INPUTS, 'video2.mp4')
    output_trans = os.path.join(DATA_OUTPUTS, 'trans')
    os.makedirs(output_trans, exist_ok=True)
    transcoder1(source_path, os.path.join(output_trans, 'transcode1.mp4'))