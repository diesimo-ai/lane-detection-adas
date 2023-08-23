# File : lanes_launch.py 
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
# Afondiel  |  22.08.2023 | Last modification 

import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
# all namespaces from img_processing module are now visible here
import img_processing


def start_lane_det(img_frame):
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

    # Read the frame/image and return a multidimensional matrix/vector of the frame/image pixels
    cap = cv2.VideoCapture(img_frame)
    
    # main loop
    while(cap.isOpened()):
        
        # read realtime capture video signal for camera any other sensors ...
        _, frame = cap.read()
        """
        step 1. & . 2 & .3  : Identify edges with Canny Fonctions: 
            - Change the gradient
                -- 0 - 15 : small change
                -- 0 - 255 : strong change
            - calculation total pixel number in the frame/image : (x : widght , y : height) => matrix[widght][height]
            - It can be represented as Math function f(x,y) and use operator to change the intensity of the pixel
            - une derivative(f(x,y)) to change the intensity of the pixel of the frame/image
            - All this procedure is used by the canny function which detects the pixel frame/image with quick intensity 
            change by comparing thresholds values  
        """
        canny_frm = img_processing.canny(frame)

        # 4. cropped frame/image with the mask
        cropped_frm = img_processing.region_of_interest(canny_frm) 

        # 5. Apply hough transform (r , teta) : shall be small for better precision
        #  HoughLinesP parameters :  r = 2 pixels , teta=1 degree, threshold = 100, empty array, ...
        lines = cv2.HoughLinesP(cropped_frm, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5 )
        
        # 6. optimizing
        # average multiples slope in the lines to a single slope line
        averaged_lines = img_processing.average_slope_intercept(frame, lines)
        # display line frame/image
        line_frm = img_processing.display_lines(frame, averaged_lines)

        # merged the gradient frame/image into the colored frame/image
        combo_frm = cv2.addWeighted(frame, 0.8, line_frm, 1, 1)
        # Creates a window to display the line frame/image
        cv2.imshow('result', combo_frm)
        # Display the frame/image during 1ms and abort the system if the a keyboard is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
        