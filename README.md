![GitHub](https://img.shields.io/github/license/afondiel/lanes-detection-adas)
# Lane Detection for ADAS systems

## Overview

This is a real time self-driving project for lane detection applied computer vision techniques.

- `input`
  - a single image/frame (.jpeg, .png ...)
  - video stream : 
    - static capturing from a recorded video of the scene
    - dynamic capturing from a camera (@todo)
- `output`
  - Real time lane detection monitoring

This version is NOT yet availaible to work with the camera, robots or even real vehicles, but to be done soon.
## Applications

- Path planning
- Vehicle Lateral Control for Self-driving cars
 ## Libraries depedencies

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

## Contrubution

- Coming upgrades : 

```
`@TODO tasks & features`
- add a logger for debugging and logging results
- add camera (sensor module) for handling camera config and 
- Test with camera in a dynamic environment (car or robot)
- add green marker between two lanes
- add different color between lane departure and inside lane
```


# References

- [Towards Data Science article by Raj Uppala](https://towardsdatascience.com/advanced-lane-detection-for-autonomous-vehicles-using-computer-vision-techniques-f229e4245e41)
- [Computer vision resources](https://github.com/afondiel/research-notes/tree/master/computer-vision-notes/documentation)

 
