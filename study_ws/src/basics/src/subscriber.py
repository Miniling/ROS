#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(msg):
    print(msg.data)
    pass

rospy.init_node('topic_publisher')  # 
pub = rospy.Publisher('counter', Int32, callback)
rospy.spin()