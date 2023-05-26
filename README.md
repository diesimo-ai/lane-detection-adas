![GitHub](https://img.shields.io/github/license/afondiel/lanes-detection-adas)
# Lane Detection for Self-Driving Cars & ADAS Systems

## Overview

A real-time lane detection applied computer vision techniques and deep learning.

- `input`
  - a single image/frame (.jpeg, .png ...)
  - video stream : 
    - static capturing from a recorded video of the scene
    - dynamic capturing from a camera (@todo)
- `output`
  - Real time lane detection monitoring

## Applications

- Environment Perception
- Motion Planning
- Vehicle Lateral Control
- Vehicle Longitudinal Control

 ## Requirements

```
conda install -c conda-forge --file requirements.txt
```
or

```
pip install -r requirements.txt
```


## Usage

To start the system
```python 
python main.py
```

## Coming Upgrade Tasks & features

`@TODO-List :`
```
- add a CNN model configuration & testing
- add a logger for debugging and logging results
- add camera (sensor module) for handling camera config and 
- Test with camera in a dynamic environment (car or robot)
- add green marker between two lanes
- add different color between lane departure and inside lane
- Add Unit testing
```

## Release History

- @TODO


 
