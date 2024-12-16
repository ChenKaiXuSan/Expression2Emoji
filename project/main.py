#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: /Users/chenkaixu/Expression2Emoji/project/main.py
Project: /Users/chenkaixu/Expression2Emoji/project
Created Date: Monday December 16th 2024
Author: Kaixu Chen
-----
Comment:

Have a good code time :)
-----
Last Modified: Monday December 16th 2024 12:37:10 pm
Modified By: the developer formerly known as Kaixu Chen at <chenkaixusan@gmail.com>
-----
Copyright (c) 2024 The University of Tsukuba
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
"""

from pathlib import Path
from utils.youtube_dl import download_youtube_video


if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=LQTVChVWi3w&list=PLXQgvG0bchMO3xLYamhjBaAYV0hBsakkh"  # 替换为实际视频链接
    output_path = Path("data")

    downloaded_video_path = download_youtube_video(youtube_url, output_path)
    print(downloaded_video_path)
