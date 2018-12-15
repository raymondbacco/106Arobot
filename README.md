# EECS 106A Final Project

After pulling this repo, the following packages need to be added to their respective folders in catkin_ws/src

* [Freenect_Stack](https://github.com/ros-drivers/freenect_stack.git)
* [Libfreenect](https://github.com/OpenKinect/libfreenect.git)
* [AR_Track_Alvar](https://github.com/ros-perception/ar_track_alvar.git)
* [RGBD__Launch](https://github.com/ros-drivers/rgbd_launch.git)

Then, a roscore must be started and the kinect and ar_track_alvar packages must be launched.

Finally, to have the robot move to an AR tag and pick something up, navigate to catkin_ws/src and run the command
```Python
python RoverGoSmooth.py
```
and wait for the program to prompt you for which AR-tag to go to. Type in the number of the tag and hit enter.
