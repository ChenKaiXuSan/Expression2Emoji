#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
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
'''

import cv2

# Load the pre-trained Haar Cascade XML file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image
image_path = 'data/face_sample.JPG'  # Replace with your image path
image = cv2.imread(image_path)

# Convert the image to grayscale (Haar Cascades work on grayscale images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Show the output image
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally save the output image
output_path = 'output_image.jpg'
cv2.imwrite(output_path, image)