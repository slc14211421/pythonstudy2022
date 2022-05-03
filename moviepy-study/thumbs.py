# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/2 23:29
Author: Lison Song

使用 moviepy 生成视频 缩略图的测试
"""
import os
import subprocess
import uuid

from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
from datetime import datetime

source_path = os.path.join(SAMPLE_INPUTS, 'video1.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-half-second")

os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)
os.makedirs(thumbnail_per_half_second_dir, exist_ok=True)


def thumbs_per_second(source_path, thumbnail_dir):
    '''
    每秒生成一张缩略图
    :param source_path: 视频文件路径
    :param thumbnail_dir: 缩略图存放路径
    :return: None
    print：
    FUNC thumbs_by_second Run time :57 seconds
    '''
    starttime = datetime.now()
    clip = VideoFileClip(source_path)
    clip = clip.resize(width=720)
    duration = clip.duration  # clip.reader.duration
    max_duration = int(duration) + 1
    for i in range(0, max_duration):
        frame = clip.get_frame(i)
        # print(frame) # np.array numpy array # inference
        new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
        # print(f"frame at {i} seconds saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)
    endtime = datetime.now()
    print(f"FUNC thumbs_by_second Run time :{(endtime - starttime).seconds} seconds")

def thumbs_per_frame(source_path, thumbnail_dir):
    '''
    每一帧生成一张缩略图
    :param source_path:
    :param thumbnail_dir:
    :return:
    '''
    starttime = datetime.now()
    clip = VideoFileClip(source_path)
    fps = clip.reader.fps
    clip = clip.resize(width=720)
    for i, frame in enumerate(clip.iter_frames()):
        current_ms = int((i / fps) * 1000)
        new_img_filepath = os.path.join(thumbnail_dir, f"{current_ms}.jpg")
        # print(f"frame at {i} seconds saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)
    endtime = datetime.now()
    print(f"FUNC thumbs_per_frame Run time :{(endtime - starttime).seconds} seconds")

def thumbs_per_half_second(source_path, thumbnail_dir):
    '''
    每半秒生成一张缩略图
    :param source_path:
    :param thumbnail_dir:
    :return:
    '''

    starttime = datetime.now()
    clip = VideoFileClip(source_path)
    fps = clip.reader.fps
    clip = clip.resize(width=720)
    fphs = int(fps / 2.0)
    for i, frame in enumerate(clip.iter_frames()):
        if i % fphs == 0:
            current_ms = int((i / fps) * 1000)
            new_img_filepath = os.path.join(thumbnail_dir, f"{current_ms}.jpg")
            # print(f"frame at {i} seconds saved at {new_img_filepath}")
            new_img = Image.fromarray(frame)
            new_img.save(new_img_filepath)

    endtime = datetime.now()
    print(f"FUNC thumbs_per_half_second Run time :{(endtime - starttime).seconds} seconds")



def thumbs_per_frame_interval_by_ffmpeg(source_name, pic_path, frame_interval=30):
    '''
    :param source_name: str 抽帧视频路径
    :param pic_path: str 抽帧图片存放瑞路径
    :param frame_interval: int 间隔多少帧抽取一次
    :return: list 抽帧图片信息的list
    -1 处理失败
    FUNC thumbs_per_frame_interval_by_ffmpeg Run time :9 seconds
    '''
    starttime = datetime.now()
    result = []
    picpath = os.path.join(pic_path, str(uuid.uuid1()))
    os.makedirs(picpath, exist_ok=True)
    dest = os.path.join(picpath, '%08d.jpg')
    parameter = f"select=not(mod(n\,{frame_interval})),showinfo"
    cmdlist = ["ffmpeg", "-i", source_name, "-s 720*405 -vsync 0 -vf ", parameter, " -f image2", dest]
    cmd = ' '.join(cmdlist)
    print(cmd)
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = str(line.strip())
        ## 筛选出包含 帧信息的日志进行处理
        if line.find("Parsed_showinfo") != -1 and line.find("pts_time") != -1:
            print(line)
            # pic_info = ffmpeg_frame_showinfo_analysis(line,picpath)
            # if pic_info != -1:
            #     result.append(pic_info)
    # print(p.returncode)
    if p.returncode != 0:
        result = -1
    endtime = datetime.now()
    print(f"FUNC thumbs_per_frame_interval_by_ffmpeg Run time :{(endtime - starttime).seconds} seconds")
    return result


def main():
    clip = VideoFileClip(source_path)
    print(clip.reader.fps)  # frames per second
    print(clip.reader.nframes)
    print(clip.duration)  # seconds
    duration = clip.duration  # clip.reader.duration
    # 每秒抽取一帧
    max_duration = int(duration) + 1
    for i in range(0, max_duration):
        frame = clip.get_frame(i)
        # print(frame) # np.array numpy array # inference
        new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
        # print(f"frame at {i} seconds saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)

    print(clip.reader.fps)  # frames per second
    print(clip.reader.nframes)

    fps = clip.reader.fps
    nframes = clip.reader.nframes
    seconds = nframes / (fps * 1.0)
    ## 按帧 抽取
    for i, frame in enumerate(clip.iter_frames()):
        # print(frame) # np.array numpy array # inference
        if i % fps == 0:
            current_ms = int((i / fps) * 1000)
            new_img_filepath = os.path.join(thumbnail_per_frame_dir, f"{current_ms}.jpg")
            # print(f"frame at {i} seconds saved at {new_img_filepath}")
            new_img = Image.fromarray(frame)
            new_img.save(new_img_filepath)
    ## 只抽取一半
    for i, frame in enumerate(clip.iter_frames()):
        # print(frame) # np.array numpy array # inference
        fphs = int(fps / 2.0)
        if i % fphs == 0:
            current_ms = int((i / fps) * 1000)
            new_img_filepath = os.path.join(thumbnail_per_half_second_dir, f"{current_ms}.jpg")
            # print(f"frame at {i} seconds saved at {new_img_filepath}")
            new_img = Image.fromarray(frame)
            new_img.save(new_img_filepath)


if __name__ == '__main__':
    # main()
    # thumbs_per_second(source_path, thumbnail_dir)
    # thumbs_per_frame(source_path, thumbnail_per_frame_dir)
    # thumbs_per_half_second(source_path, thumbnail_per_half_second_dir)
    '''
    对比测试结果 ffmpeg 抽针的效率是  使用 moviepy+pillow image 的6倍  
    '''
    thumbs_per_frame_interval_by_ffmpeg(source_path, thumbnail_dir)
