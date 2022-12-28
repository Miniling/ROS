#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32, String
from geometry_msgs.msg import Twist

def callback(msg):
    print(msg.data)
    cahnge_data = 'min : '+str(msg.data)  # string type data
    pub.publish(cahnge_data)

rospy.init_node('topic_subscriber')  # subscribe from publisher
sub = rospy.Subscriber('counter', Int32, callback)
pub = rospy.Publisher('min_topic', String, queue_size=1)

# Passive
rospy.spin()