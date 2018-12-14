# Additional Materials

## Script to Use Motor Controller and AR Tracker

```python
import tf2_ros
import rospy
import numpy as np
import sys
import os
import RPi.GPIO as GPIO
import PiMotor
import time
import grabBlock as grabber

GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)

class RoverGo:

	def __init__(self):
		# self.pose = Pose()
		rospy.init_node('tf_listener', anonymous=True)
		self.rover_frame = "camera_link"
		self.goal_frame = None
		self.tfBuffer = tf2_ros.Buffer()
		self.tfListener= tf2_ros.TransformListener(self.tfBuffer)
		self.rate = rospy.Rate(10)
		self.left_motor = PiMotor.Motor("MOTOR1",1)
		self.right_motor = PiMotor.Motor("MOTOR2",1)
		self.distance_tolerance = 0.5
                self.angle_tolerance = 0.25
		self.goalReached = False

	def dist(self, goalT):
		return np.sqrt(goalT.x * goalT.x + goalT.y * goalT.y)

	def angle(self, goalT):
		return np.arctan(goalT.y / goalT.x)

	def currTrans(self):
		trans = self.tfBuffer.lookup_transform(self.rover_frame, self.goal_frame, rospy.Time(0)).transform
	        #print("Distance:", self.dist(trans.translation), "Angle:", self.angle(trans.translation))
                #print(trans.translation)
                return trans

	def photo_left(self):
		return GPIO.input(10)

	def photo_right(self):
		return GPIO.input(8)

	def leftForward(self, val):
                #return
                self.left_motor.forward(val)

	def rightForward(self, val):
                #return
		self.right_motor.forward(val)

	def leftReverse(self, val):
                #return
		self.left_motor.reverse(val)

	def rightReverse(self, val):
                #return
		self.right_motor.reverse(val)

	def stopMotors(self):
		self.left_motor.stop()
		self.right_motor.stop()

	def drive(self, goalT, error_func, tolerance, left_motor_func, right_motor_func, delta_input=5, max_ticks=35):
		encoderTolerance = 3
		photo_total_right = 0
		photo_total_left = 0
		photo_right_prev = self.photo_right()
		photo_left_prev = self.photo_left()
		right_input = 100
		left_input = 70
                start_time = rospy.get_time()
		while goalT is None or abs(error_func(goalT)) > tolerance:
		    photo_right_current = self.photo_right()
		    photo_left_current = self.photo_left()
		    if (photo_right_current != photo_right_prev):
		        photo_total_right += 1
		    if (photo_left_current != photo_left_prev):
		        photo_total_left += 1
		    photo_right_prev = photo_right_current
		    photo_left_prev = photo_left_current
                    if max(photo_total_left, photo_total_right) > max_ticks:
                        break
		    delta = photo_total_left - photo_total_right
		    if (abs(delta) > encoderTolerance):
		    	right_input += delta
		    	if right_input > 100:
		    		right_input = 100
		    	elif right_input < 0:
		    		right_input = 0
                    left_motor_func(left_input)
		    right_motor_func(right_input)
                    try:
		        goalT = self.currTrans().translation
                    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                        goalT = None
		self.stopMotors()
                rospy.sleep(3)
		#print("Right photo interruptor: " + str(photo_total_right))
		#print("Left photo interruptor: " + str(photo_total_left))

	def driveStraight(self, goalT):
		print("Driving straight...")
		self.drive(goalT, self.dist, self.distance_tolerance, self.leftForward, self.rightForward)

	def turnLeft(self, goalT):
		print("Turning left...")
		self.drive(goalT, self.angle, self.angle_tolerance, self.leftReverse, self.rightForward, max_ticks=5)

	def turnRight(self, goalT):
		print("Turning right...")
		self.drive(goalT, self.angle, self.angle_tolerance, self.leftForward, self.rightReverse, max_ticks=5)

	def goToTag(self, goal_frame):
                trans = None
                prevTrans = None
		self.goal_frame = goal_frame
		while not rospy.is_shutdown() and not self.goalReached:
			try:
                                if trans is not None:
                                    prevTrans = trans
		                trans = self.currTrans()
		                goalTranslation = trans.translation

                                if self.dist(goalTranslation) <= self.distance_tolerance and self.angle(goalTranslation) <= self.angle_tolerance:
					self.goalReached = True

				if not self.goalReached:
                                        currAngle = self.angle(goalTranslation)
				        if np.abs(currAngle) >= self.angle_tolerance:
					        if currAngle < 0:
						        self.turnRight(goalTranslation)
					        else:
						        self.turnLeft(goalTranslation)
				        elif self.dist(goalTranslation) >= self.distance_tolerance:
					        self.driveStraight(goalTranslation)

			except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
				print("Tag not detected. Searching...")
                                if prevTrans is not None:
                                    prevAngle = self.angle(prevTrans.translation)
                                    if prevAngle > 0:
                                        self.turnLeft(None)
                                    else:
                                        self.turnRight(None)
                                else:
                                    self.turnRight(None)
                                rospy.sleep(5)
                self.stopMotors()
		print("We made it folks")
                grabber.grab()


if __name__ == '__main__':
	r = RoverGo()
	numS = input("Which tag would you like?  ")
	tag = 'ar_marker_' + str(numS)
	r.goToTag(tag)
```

## Our Code

The rest of our code can be found on our [GitHub](https://github.com/raymondbacco/106Arobot). Some software resources that we used are ROS Kinetic, Freenect_Stack (an open source kinect package), and Ar_Track_Alvar. 

## Hardware Data Sheets

* [Raspberry pi 3 B+](https://static.raspberrypi.org/files/product-briefs/Raspberry-Pi-Model-Bplus-Product-Brief.pdf)
* [7 “ Raspberry Pi Touchscreen](http://www.farnell.com/datasheets/1958036.pdf)
* [Xbox 360 Kinect](https://zoomicon.wordpress.com/2015/07/28/kinect-for-xbox-360-and-kinect-for-windows-kfw-v1-specs/)
* [PCA 9685 16 channel Servo Controller](https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf)
* [SB Components Motor Shield](https://sb-components.co.uk/motor-shield.html)
* [Mg966r 4.8V-7.2V Servo Motor](https://www.electronicoscaldas.com/datasheet/MG996R_Tower-Pro.pdf)
* [SunFounder Photo-interrupter Sensor Module](https://www.sunfounder.com/learn/lesson-12-photo-interrupter-sensor-kit-v2-0-for-b-plus.html)

## Pictures
![Arm Mount](/assets/robot_images/arm_mount.jpg)
![Back Right View](/assets/robot_images/back_right_view.jpg)
![Bottom Battery Holder](/assets/robot_images/bottom_battery_holder.jpg)
![Front Battery Holder](/assets/robot_images/front_battery_holder.jpg)
![Front View](/assets/robot_images/front_view.jpg)
![Kinect Mount](/assets/robot_images/kinect_mount.jpg)
![Left Side View](/assets/robot_images/left_side_view1.jpg)
![Photo Interrupter Mount](/assets/robot_images/photo_interupter_mount.jpg)
![Right Side View](/assets/robot_images/right_side_view.jpg)
![Screen Mount](/assets/robot_images/screen_mount.jpg)

