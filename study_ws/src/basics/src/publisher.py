#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')  # init rospy: 'topic_publisher'

pub = rospy.Publisher('counter', Int32, queue_size=10)   # publish 'counter'
rate = rospy.Rate(10)   # publishing rate(Hz)
count = 0

# Active
while not rospy.is_shutdown():
    pub.publish(count)
    count += 1
    rate.sleep()