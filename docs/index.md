# Introduction


## Abstract

Our original end goal was to create a robot with an arm that can go and retrieve a specific object from among a selection of a few different objects. Each object is labelled with a different AR-tag and the user will be able to tell the robot which AR-tag's object to retrieve.

## Project Description

Our robot uses a camera to read each object’s AR-tag and decide which object the user has asked for and then retrieve it. It is able see and recognize different AR-tags and then accurately locate the desired tag and go to the object associated with the tag. Then using its arm our robot then picks up the the object. Our project is interesting because it makes use of some computer vision and controls to have the robot locate a desired object and then be able to accurately navigate to it. Our robot incorporates sensing through the use of a  Kinect to see the objects and tags, it incorporates planning by seeing where the object is in relation to its arm and then using inverse kinematics be able to move its arm into a position to pick up the object, and it incorporates actuation through the use of our arm and wheels. Because we built our own robot and hardware from scratch, we had to make our own controls for the motors so that the robot would be able to navigate itself precisely and we had to figure out how to connect and calibrate our own kinect camera and have the robot react according to what the camera sees. 

## Real-World Applications

Our project was created with the idea of making a robot that can help someone retrieve objects from around their home. There are many people, such as those with disabilities, who have difficulty getting around the house and a robot that could go and retrieve some desired object for the person could help make their lives easier.
