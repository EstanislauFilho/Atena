#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def detecta_bordas_pista(img):
	# Color thresholding
	ret,thresh = cv2.threshold(img,145,250,cv2.THRESH_BINARY_INV)
	
	# Find the contours of the frame
	contours, hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
	
	if len(contours) > 0:
		c = max(contours, key=cv2.contourArea)
		
		M = cv2.moments(c)

		cx = int(M['m10']/M['m00'])

		cy = int(M['m01']/M['m00'])

		cv2.line(img,(cx,0),(cx,420),(255,0,0),1)

		cv2.line(img,(0,cy),(680,cy),(255,0,0),1)

		cv2.drawContours(img, contours, -1, (0,255,0), 1)

		return img, cx