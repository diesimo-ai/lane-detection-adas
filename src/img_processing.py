# File : img_processing.py 
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

import cv2
# from cv2 import cv2
import numpy as np


def canny(image):
    """ 
    - DESC : detects the pixel image with quick intensity change by comparing thresholds values  
    - INPUT : image
    - OUTPUT : returns a gradiented image
    """
    gray = gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(image):
    """ 
    - DESC :  creates a mask on a canny image specific zone
    - INPUT : image
    - OUTPUT : mask region to be processed
    """
    height = image.shape[0]
    # draw the dimension of the interest to be applied (use matplotlib)
    # the dimension shall be realist and close enough to have a good accurracy  
    polygons = np.array([
    [(200, height), (1100, height), (550, 250)]
    ])
    # put all pixels to zero (black background)
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):
    """ 
    - DESC :  displays the number of lines 
    - INPUT : image, lines
    - OUTPUT : return reconstructed lines of the image 
    """
    # transform the image background to black
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            # print a group of matrix 1x4 which represent the numbers of line position in the original image, need to be reshaped
            # 2D : [[x1, y1, x2, y2]] => 1D : [x1, y1, x2, y2] 
            # print(line)
            #reshaping the matrix and draw the line
            x1, y1, x2, y2 = line.reshape(4)
            # line parameters :  [x1, y1, x2, y2] , BGR space: (Blue, Green, Red), tickness : 10 
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image

def average_slope_intercept(image, lines):
    """ 
    - DESC :  determines the average slope of the left and right line 
    - INPUT : image, lines
    - OUTPUT : returns a list of average slope of the left and right line
    """
    # coordinate of the average line on the left
    left_fit = []
    # coordinate of the average line on the right
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        # extract the vector coeficients of coordinates of the image (b and m of "y=m*x+b")
        # fit polynom of degre 1 into (x and y) point return  the vector coeficients of coordinates 
        parameters = np.polyfit((x1, x2),(y1, y2), 1)
        # print(parameters)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    # averaging starting vertically from the bottom of the image
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_average )
    right_line = make_coordinates(image, right_fit_average )

    return np.array([left_line, right_line]) 
    
    print(left_fit_average)
    print(right_fit_average)

def make_coordinates(image, line_parameters):
    """ 
    - DESC :  Creates a coordinates according of the image and line parameters values
    - INPUT : image, line_parameters
    - OUTPUT : returns an array of the parameters extracted from the polynom
    """
    # prevent reading unknow values such as np.nan types
    try:
        slope, intercept = line_parameters
    except TypeError:
        slope, intercept = 0.001, 0
    # slope, intercept = line_parameters

    # getting the shape of the image
    # print(image.shape)
    y1 = image.shape[0]
    # 704*(3/5)
    y2 = int(y1*(3/5))
    # x = (y - b)/m which iqual to (y - intercept)/m 
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])