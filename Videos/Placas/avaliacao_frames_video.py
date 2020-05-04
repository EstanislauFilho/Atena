#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:40:46 2020

@author: estanislau
"""


import cv2
import glob


for i in sorted(glob.glob('frames_video_teste_1/*.jpg')):  
    #print(i)
    imagem = cv2.imread(i)
    
    cv2.imshow("Apresenta Imagens", imagem)
    cv2.waitKey(1000)

cv2.destroyAllWindows()	