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
# Afondiel  |  21.12.2022 | Last modification 

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
# all namespaces from the img_processing module are now visible here
import modules.img_processing
import modules.lanes_launch

if __name__ == "__main__" :
    # start the lanes
    lanes_start()
