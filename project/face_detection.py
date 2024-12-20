#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: /Users/chenkaixu/Expression2Emoji/project/face_detection.py
Project: /Users/chenkaixu/Expression2Emoji/project
Created Date: Monday December 16th 2024
Author: Kaixu Chen
-----
Comment:

Have a good code time :)
-----
Last Modified: Monday December 16th 2024 12:48:53 pm
Modified By: the developer formerly known as Kaixu Chen at <chenkaixusan@gmail.com>
-----
Copyright (c) 2024 The University of Tsukuba
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
"""


import cv2


def detect_faces_in_video(video_path: str):
    # 加载预训练的人脸检测模型
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # 打开视频文件
    video_capture = cv2.VideoCapture(video_path)

    while video_capture.isOpened():
        # 逐帧读取视频
        ret, frame = video_capture.read()
        if not ret:
            break

        # 转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 检测人脸
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        # 绘制人脸位置
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 显示结果帧
        cv2.imshow("Video", frame)

        # 按q键退出
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # 释放视频捕获对象
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    # 打开视频文件
    video_path = "data/[1996年春晚]小品：打工奇遇，表演：赵丽蓉 巩汉林 | CCTV春晚.mp4"
    video_capture = cv2.VideoCapture(video_path)

    detect_faces_in_video(video_path)