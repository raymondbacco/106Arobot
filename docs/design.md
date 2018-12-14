# Design

## Design Criteria

Our group's primary design goal was to build our own robot from scratch that could run completely on its own without the help of an external computer. We decided we wanted our robot to be able to drive itself around a room and attempt to grab things via an arm. In terms of functionality, we eventually decided we would have our robot identify and retrieve a particular object from a small selection of objects.

## Our Design

Our robot needed to accomplish 3 tasks in order to retrieve an object. First, it had to see the object.  In order for the robot to see the object, we chose to use a kinect camera and AR-tag recognition. Once the target was visible, we needed the robot to drive to the target. To accomplish this, we wrote a python script, that includes a proportional controller to drive the robot straight, as well as some logic to help the robot decide which direction it should drive. Finally, we had the robot attempt to pick up the target object. This was also accomplished via a simple python script that hardcoded the arm to attempt a grab.

## Design Choices and Tradeoffs

Ideally, our robot would be able to identify objects without the use of AR-tags, but for simplicity, we decided to use them. Originally, we wanted to place AR-tags directly on the target objects, but because we ultimately chose to use a static camera, the robot could not look down when it got close to the target object and as a result could not recognize when it should attempt a grab. Instead, we chose to use large standing AR-tags near the desired objects that served as a guide for the robot. Because the robot arm is hardcoded, there is no need to see the actual object, the robot only needs to get close. As a result, the large standing AR-tags are sufficient for our current implementation. However, if we were to ever implement a more sophisticated utilization of the robot arm, the large AR-tags would no longer be sufficient and we would have to reformulate how the robot locates its target objects. We also chose to have our robot drive in small discrete steps with short pauses in between because when the robot would move continuously, the AR tracking would not update fast enough to have any sort of accuracy. Driving in discrete steps does not look as impressive, but it greatly increases the accuracy of the robot as it drives to its target. Finally, as previously mentioned, we chose to hardcode the robot arm. This choice was made primarily due to time constraints. A more sophisticated utilization of the robot arm would greatly increase the accuracy of the robot in picking up its target object.

## Design Choices' Impact

The incorporation of AR-tags in our design could in theory be utilized in a real-world application, however this would not be ideal, as it would be much more robust and efficient to have the robot recognize the actual target objects. Having the robot drive in discrete steps was a vital design choice that greatly improved the accuracy of our robot. Having the robot drive continuously would result in a more polished looking final product, but accuracy is far more important for any real-world application. Finally, utilizing the robot arm in a more sophisticated way would improve the accuracy of the robot and the robustness of the overall project in a real-world application, but for our design criteria a hardcoded arm was sufficient.


