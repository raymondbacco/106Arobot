# Introduction


## Abstract

Our original end goal was to create a robot with an arm that can go and retrieve a specific object from among a selection of a few different objects. Each object is labelled with a different AR-tag and the user will be able to tell the robot which AR-tag's object to retrieve.

## Project Description

Our robot uses a camera to read each object’s AR-tag and decide which object the user has asked for and then retrieve it. It is able see and recognize different AR-tags and then accurately locate the desired tag and go to the object associated with the tag. Then using its arm our robot then picks up the the object. Our project is interesting because it makes use of some computer vision and controls to have the robot locate a desired object and then be able to accurately navigate to it. Our robot incorporates sensing through the use of a  Kinect to see the objects and tags, it incorporates planning by seeing where the object is in relation to its arm and then using inverse kinematics be able to move its arm into a position to pick up the object, and it incorporates actuation through the use of our arm and wheels. Because we built our own robot and hardware from scratch, we had to make our own controls for the motors so that the robot would be able to navigate itself precisely and we had to figure out how to connect and calibrate our own kinect camera and have the robot react according to what the camera sees. We originally planned for the tags to be on the objects themselves but with the way the camera was positioned, the objects were too low for it to see the tags and we also had issues with getting the robot to distinguish small AR-tags from each other so we had to make large ones and place the objects in front of them. We also had various problems with downloading ROS and some packages since we were working exclusively on our personal computers instead of lab computers. 

## Real-World Applications

Our project was created with the idea of making a robot that can help someone retrieve objects from around their home. We used AR-tags to distinguish the different objects but ideally we would want to program the robot to eventually be able to identify different objects without AR-tags or be able to have it see and recognize smaller tags that we could attach to the objects.

