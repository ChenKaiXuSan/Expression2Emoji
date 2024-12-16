#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: /Users/chenkaixu/Temp_Feedback/utils/youtube_dl.py
Project: /Users/chenkaixu/Temp_Feedback/utils
Created Date: Saturday December 14th 2024
Author: Kaixu Chen
-----
Comment:

Have a good code time :)
-----
Last Modified: Saturday December 14th 2024 11:53:07 pm
Modified By: the developer formerly known as Kaixu Chen at <chenkaixusan@gmail.com>
-----
Copyright (c) 2024 The University of Tsukuba
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
"""

from pathlib import Path
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_youtube_video(url: Path, save_path: Path="downloaded_video.mp4"):

    url = Path(url)
    save_path = Path(save_path)
    
    if save_path.exists() is False:
        save_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        yt = YouTube(str(url), on_progress_callback=on_progress)
        video_stream = yt.streams.get_highest_resolution()
        # video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        print(f"Downloading: {yt.title}")
        video_stream.download(filename=str(save_path/yt.title) + ".mp4")
        print(f"Video downloaded and saved as {save_path}")
        return save_path
    except Exception as e:
        print(f"Error: {e}")
        return None



# # 示例调用
# if __name__ == "__main__":
#     youtube_url = "https://www.youtube.com/watch?v=v_w2BBQ4NI8"  # 替换为实际视频链接
#     downloaded_video_path = download_youtube_video(youtube_url)