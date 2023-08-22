# File : main.py 
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
# local packages
import src.img_processing 
from src.launch_lane import start_lane_det

# load the input frame 
frame_path = os.path.relpath('.\\data\\driving_video.mp4',  os.path.dirname(__file__))


if __name__ == "__main__" :

    # launch the system
    start_lane_det(frame_path)
