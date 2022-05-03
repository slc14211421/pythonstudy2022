# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/3 1:49
Author: Lison Song
"""
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *  # ImageClip
from PIL import Image


def dir_video_per_second(thumbnail_dir, output_video):
    this_dir = os.listdir(thumbnail_dir)
    filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("jpg")]
    '''
    filepaths = []
    for fname in this_dir:
        if fname.endswith("jpg"):
            path = os.path.join(thumbnail_dir, fname)
            filepaths.append(path)

    print(filepaths)
    clip = ImageSequenceClip(filepaths, fps=1)
    clip.write_videofile(output_video)
    '''
    clip = ImageSequenceClip(filepaths, fps=24)
    clip.write_videofile(output_video)


def dir_2video_per_frame(thumbnail_dir, output_video):
    directory = {}

    for root, dirs, files in os.walk(thumbnail_dir):
        for fname in files:
            filepath = os.path.join(root, fname)
            try:
                key = float(fname.replace(".jpg", ""))
            except:
                key = None
            if key != None:
                directory[key] = filepath

    new_paths = []
    for k in sorted(directory.keys()):
        filepath = directory[k]
        new_paths.append(filepath)

    clip = ImageSequenceClip(new_paths, fps=30)
    clip.write_videofile(output_video)
    #
    # my_clips = []
    # for path in list(new_paths):
    #     frame = ImageClip(path)
    #     # print(frame.img) # numpy array
    #     my_clips.append(frame.img)
    #
    # clip = ImageSequenceClip(my_clips, fps=22)
    # clip.write_videofile(output_video)



if __name__ == '__main__':
    thumbnail_dir = os.path.join(os.path.join(SAMPLE_OUTPUTS, "thumbnails"), '71d4e1b1-ca40-11ec-9e28-00e04ce10c56')
    output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs_per_second.mp4')
    # dir_video_per_second(thumbnail_dir, output_video)

    thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
    output_video2 = os.path.join(SAMPLE_OUTPUTS, 'thumbs_per_frame.mp4')
    dir_2video_per_frame(thumbnail_per_frame_dir, output_video2)
