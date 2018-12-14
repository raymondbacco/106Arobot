---
order: 40
---

# Conclusion

Our project did fulfill most of our goals and did hit our minimum success requirement. The robot's motors were controlled so that it could precisely and accurately navigate itself to a specific location without wavering off course and the camera was able to find and track AR-tags consistently. Unfortunately we did not have time to implement the inverse kinematics code for the robot's arm as we intended so the arm is hardcoded to extend to the same spot in front of the robot every time. Because of this, we instead programmed the robot to stop a certain distance away from the AR-tag and position itself so that the object would be in reach of its arm. 

## Difficulties We Faced

Since we were working on our personal computers instead of the lab computers, we needed to download ROS and any packages we needed. We had some dependency errors when downloading ROS but was able to fix it by switching from Raspian to Unbuntu. We also had some issues trying to download packages for our project and needed to go on GitHub and manually download each package ourselves.

We also had some problems when trying to calibrate our camera. We first tried to use a USB webcam but had some problems when calibrating it and could not get it to work properly with the Raspberry Pi. We then switched to using a kinect and after some difficulties again involving downloading packages, we were able to get the camera to connect to the Pi and were then able to calibrate it. 

When trying to control our motors, we had some trouble getting the robot to move smoothly in a straight line. We implemented a controller that used encoders to measure the ticks of the motors and found the difference between the speeds of the two motors. If the difference between the two became larger than a certain threshold, it would either speed up or slow down one of the motors in order to rebalance them. The controller at first caused the robot to be very shaky when moving and made it constantly jerk left and right in order to force its trajectory to be straight. After spending a long time playing with values and different kinds of controllers, we were finally able to make the robot move straight smoothly. 

We also originally planned for the tags to be on the objects themselves but with the way the new camera was positioned, the objects were too low for it to see the tags and we also had issues with getting the robot to distinguish small AR-tags from each other so we had to make large ones and place the objects in front of them. 

## Potential Improvements

We used AR-tags to distinguish the different objects but ideally we would want to program the robot to eventually be able to identify different objects without AR-tags or be able to have it see and recognize smaller tags that we could attach to the objects.

We would also want to find a way to make the AR-tag tracker update and find the tf transformations faster. At the moment, our robot pauses every few seconds in order to find the tag and recalculate the transforms and see how far and at what angle the tag is after the robot has moved so that it will stay on track to get to the target.

Additionally, our robot's arm is hardcoded at the moment to always reach to the same point in front of the robot. Given more time, we would have attempted to implement a program to perform inverse kinematics on the location of the object and the arm's position and we would have also implemented controls on the arm as well so that it would reach towards the object instead of to the same spot. 

We also would have liked to make a URDF (Universal Robot Description Format) of our robot in order to use RViz MoveIt Control.
