import tf2_ros
import rospy
import numpy as np
import sys


class RoverGo:

	def __init__(self):
		self.hi = "hi"

	def goToTag(self, arg1, arg2):
		rospy.init_node('tf_listener', anonymous=True)
		tfBuffer = tf2_ros.Buffer()
		tfListener= tf2_ros.TransformListener(tfBuffer)
		while not rospy.is_shutdown():
			try:
				trans = tfBuffer.lookup_transform(arg2,arg1,rospy.Time()).transform
				translation = trans.translation
				rotation = trans.rotation
				print(translation)
			except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
				continue

if __name__ == '__main__':
	r = RoverGo()
	numS = input("Which tag would you like?  ")
	tag = 'ar_marker_'+str(numS)
	r.goToTag('camera_link',tag)
