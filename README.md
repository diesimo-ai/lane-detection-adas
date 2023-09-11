![GitHub](https://img.shields.io/github/license/afondiel/lanes-detection-adas)
# Lane Detection for ADAS & Self-Driving Cars

## Overview

This a real-time lane detection using computer vision techniques and deep learning.

The system takes a single (road) image or a recorded local video from the road and perform the following tasks:

```
1. Convert the color frame/image to grayscale for easy and quick treatment
2. Reduce noise and smooth with Gaussian Blur filter
3. Identify edges with Canny Functions : 
    - This allows to detect edges in the frame/image. By checking the intensity changes in brightness of adjecent pixels
4. Calculate the Region of interest of the lines 
5. Hough transform
6. Optimizing
```

## Application

The system has several situations and can be used in many situations:
- Lane departure warning systems
- Lane-keeping assistant technology (vehicle longitudinal & lateral control)
- Hand-free highway driving systems (during steering takeover)
- [Kodiak Robotics](https://kodiak.ai/) uses lane lines detection for its [self-driving truck (KodiakDriver)](https://kodiak.ai/technology/) stack to navigate in the world

 ## Requirements & dependency packages

```
python=3.7.*
numpy
matplotlib
opencv
opencv-contrib-python
```

To install all package from the requirements.txt file via conda:

```
conda install --file requirements.txt
```
or

```
pip install -r requirements.txt
```

## Usage

To run the system:

```python 
python main.py
```

## Upcoming features & Upgrades

`@TODO-List :`
```
- add a logger for debugging and logging results
- add camera config module for real-time applications handling
- add a SegNet or a CNN model interface to increase system accuracy  
- add green marker between two road lanes for urban/highway roads
- add different color between lane departure and inside lane
- Add Unit testing
- Test with camera in a dynamic environment (car or robot)
- CI/CD actions
```
## Contributing

If you want to help this project grow, feel free to submmit a PR.





 
