'''
给 视频加上背景音乐
https://github.com/codingforentrepreneurs/30-Days-of-Python/blob/master/tutorial-reference/Day%2015/4_mix_audio.py
'''

from conf import DATA_INPUTS, DATA_OUTPUTS
from moviepy.editor import *
## 待处理的视频
source_path = os.path.join(DATA_INPUTS, 'video_hulk.mp4')
## 待加入的音频文件 作为背景音
source_audio_path = os.path.join(DATA_INPUTS, 'audio4.mp3')

mix_audio_dir = os.path.join(DATA_OUTPUTS, "mixed-audio")
os.makedirs(mix_audio_dir, exist_ok=True)
og_audio_path = os.path.join(mix_audio_dir, 'og.mp3')
final_audio_path = os.path.join(mix_audio_dir, 'final-audio.mp3')
final_video_path = os.path.join(mix_audio_dir, 'final-mixed-audio-video.mp4')

video_clip = VideoFileClip(source_path)

## 抽取 原视频的音频并保存
original_audio = video_clip.audio
original_audio.write_audiofile(og_audio_path)

## 编辑背景音乐的时长
background_audio_clip = AudioFileClip(source_audio_path)
bg_music = background_audio_clip.subclip(0, video_clip.duration)

## 设置背景音乐的音量
# bg_music = bg_music.fx(volumex, 0.10)
bg_music = bg_music.volumex(0.10)
# bg_music.write_audiofile()
## 将原音频和背景音乐合成
final_audio = CompositeAudioClip([original_audio, bg_music])
final_audio.write_audiofile(final_audio_path, fps=original_audio.fps)


# new_audio = AudioFileClip(final_audio_path)
# final_clip = video_clip.set_audio(new_audio)

#将合成的背景音乐加入视频中
final_clip = video_clip.set_audio(final_audio)
final_clip.write_videofile(final_video_path, codec='libx264', audio_codec="aac")