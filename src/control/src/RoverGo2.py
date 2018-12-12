#!/usr/bin/env python

import tf2_ros
import rospy
import numpy as np
import sys
import os
import RPi.GPIO as GPIO
import PiMotor
import time

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
		self.distance_tolerance = 0.01
                self.angle_tolerance = 0.2
		self.goalReached = False

	def dist(self, goalT):
		return np.sqrt(goalT.x*goalT.x + goalT.y*goalT.y)

	def angle(self, goalT):
		return np.arctan2(goalT.y, goalT.x)

	def currTrans(self):
		trans = self.tfBuffer.lookup_transform(self.goal_frame, self.rover_frame, rospy.Time()).transform
		print("Distance:", self.dist(trans.translation), "Angle:", self.angle(trans.rotation))
                return trans
		# goalTranslation = trans.translation
		# goalRotation = trans.rotation

	def photo_left(self):
		return GPIO.input(10)

	def photo_right(self):
		return GPIO.input(8)

	def leftForward(self, val):
                return
                #self.left_motor.forward(val)

	def rightForward(self, val):
                return
		#self.right_motor.forward(val)

	def leftReverse(self, val):
                return
		#self.left_motor.reverse(val)

	def rightReverse(self, val):
                return
		#self.right_motor.reverse(val)

	def stopMotors(self):
		self.left_motor.stop()
		self.right_motor.stop()

	def drive(self, goalT, error_func, tolerance, left_motor_func, right_motor_func, initial_input=80, delta_input=10):
		photo_total_right = 0
		photo_total_left = 0
		photo_right_prev = self.photo_right()
		photo_left_prev = self.photo_left()
		right_input = initial_input
		left_input = initial_input
		while abs(error_func(goalT)) >= tolerance:
		    photo_right_current = self.photo_right()
		    photo_left_current = self.photo_left()
		    if (photo_right_current != photo_right_prev):
		        photo_total_right += 1
		    if (photo_left_current != photo_left_prev):
		        photo_total_left += 1
		    photo_right_prev = self.photo_right()
		    photo_left_prev = self.photo_left()

		    delta = photo_total_left - photo_total_right
		    turning_right = delta > 0
		    turning_left = delta < 0
		    if (turning_right and right_input != 100 and left_input != 0):
		        left_input -= delta_input
			right_input += delta_input
		    if (turning_left < 0 and left_input != 100 and right_input != 0):
		        left_input += delta_input
		        right_input -= delta_input
		    left_motor_func(left_input)
		    right_motor_func(right_input)
		    #print("delta: " + str(delta))
		    goalT = self.currTrans().translation
		self.stopMotors()
		#print("Right photo interruptor: " + str(photo_total_right))
		#print("Left photo interruptor: " + str(photo_total_left))

	def driveStraight(self, goalT):
		print("Driving straight...")
		self.drive(goalT, self.dist, self.distance_tolerance, self.leftForward, self.rightForward)

	def turnLeft(self, goalT):
		print("Turning left...")
		self.drive(goalT, self.angle, self.angle_tolerance, self.leftReverse, self.rightForward)

	def turnRight(self, goalT):
		print("Turning right...")
		self.drive(goalT, self.angle, self.angle_tolerance, self.leftForward, self.rightReverse)

	def goToTag(self, goal_frame):
		# rospy.init_node('tf_listener', anonymous=True)
		# tfBuffer = tf2_ros.Buffer()
		# tfListener= tf2_ros.TransformListener(tfBuffer)
		self.goal_frame = goal_frame
		while not rospy.is_shutdown() and not self.goalReached:
			try:
				# trans = tfBuffer.lookup_transform(arg2,arg1,rospy.Time()).transform
				# goalTranslation = trans.translation
				# goalRotation = trans.rotation
				trans = self.currTrans()
		                goalTranslation = trans.translation
		                goalRotation = trans.rotation

                                if self.dist(goalTranslation) <= self.distance_tolerance and self.angle(goalRotation) <= self.angle_tolerance:
					self.goalReached = True

				if not self.goalReached:
                                        currAngle = self.angle(goalTranslation)
				        if np.abs(currAngle) >= self.angle_tolerance:
					        if currAngle > 0:
						        self.turnRight(goalTranslation)
					        else:
						        self.turnLeft(goalTranslation)
				        if self.dist(goalTranslation) >= self.distance_tolerance:
					        self.driveStraight(goalTranslation)

			except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
				continue
                self.stopMotors()
		print("We made it folks")


if __name__ == '__main__':
	r = RoverGo()
	numS = input("Which tag would you like?  ")
	tag = 'ar_marker_' + str(numS)
	r.goToTag(tag)
