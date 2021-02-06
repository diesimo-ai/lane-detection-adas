# File : main_lanes.py 
#
# Description : This is a real time self-driving computer vision project intended to detect 
# 				a road lane 
#
# Libraries requirements : 
#   <cv2> : opencv standard library 
#   	- Provides functionalities for image processing
#   <numpy> : standard library
#		- Provides multidimensional arrays and linear algebra tools, optimized for speed
#   <matplotlib> :standard library 
#		- Provides scientific plotting
#
# File history :
# Afondiel  |  30.01.2021 | Creation 
# Afondiel  |  06.02.2021 | Last modification 

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
# all namespaces from the functions module are now visible here
import functions


"""
	Global approach and strategy : 
    1. Convert the original frame/image to grayscale for easy and quick treatment
    2. Reduce noise and  smooth with gaussian Blur filter
    3. Identify edges with Canny Functions : 
		- This allows to detect edges in the frame/image. By checking the intensity changes in brightness of adjecent pixels
    4. Calculate the Region of interest of the lines 
    5. Hough transform
    6. Optimizing
"""

""" 
Main : This file is the main module
"""

# get the current file
cur_path = os.path.dirname(__file__)
#input frame 
frame_path = os.path.relpath('..\\outro\\test2.mp4', cur_path)

if __name__ == "__main__" :

    # Read the frame/image and return a multidimensional matrix/vector of the frame/image pixels
    cap = cv2.VideoCapture(frame_path)
	
	# main loop
    while(cap.isOpened()):
		
		# read realtime capture video  signal for camera any other sensors ...
        _, frame = cap.read()

        """
		#1_2_3. Identify edges with Canny Fonctions: 
		Steps : 
		- Change the gradient
			-- 0 - 15 : small change
			-- 0 - 255 : strong change
		- calculation number total pixel in the frame/image : (x : widght , y : height) => matrix[widght][height]
		- It can be represented as Math function f(x,y) and use operator to change the intensity of the pixel
		- une derivative(f(x,y)) to change the intensity of the pixel of the frame/image
		- All this procedure is used by the canny function which detects the pixel frame/image with quick intensity 
		change by comparing thresholds values  
		"""
        canny_frm = functions.canny(frame)

        # 4. cropped frame/image with the mask
        cropped_frm = functions.region_of_interest(canny_frm) 
        # 5. Apply hough transform (r , teta) : shall be small for better precision
        #  HoughLinesP parameters :  r = 2 pixels , teta=1 degree, threshold = 100, empty array, ...
        lines = cv2.HoughLinesP(cropped_frm, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5 )
        
        # 6. optimizing
        # average multiples slope in the lines to a single slope line
        averaged_lines = functions.average_slope_intercept(frame, lines)
        # display line frame/image
        line_frm = functions.display_lines(frame, averaged_lines)

        # merged the gradient frame/image into the colored frame/image
        combo_frm = cv2.addWeighted(frame, 0.8, line_frm, 1, 1)
        # Creates a window to display the line frame/image
        cv2.imshow('result', combo_frm)
        # Display the frame/image during 1msn and abort the system if the a keyboard is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    