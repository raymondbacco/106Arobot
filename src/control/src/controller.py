import tf2_ros
import rospy
import numpy as np
import sys

def main(arg1,arg2):
	rospy.init_node('tf_listener', anonymous=True)
	tfBuffer = tf2_ros.Buffer()
	tfListener= tf2_ros.TransformListener(tfBuffer)
	while not rospy.is_shutdown():
		try:
			trans = tfBuffer.lookup_transform(arg2,arg1,rospy.Time())
			translation = trans.transform.translation
			rotation = trans.transform.rotation
			print("trans:")
                        print(translation)
                        print("rotation:")
                        print(rotation)
                        #distance=
                        #angle=
     		except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
			continue

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])
