#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32, String
from geometry_msgs.msg import Twist  # autonomous driving message

Twist_data = Twist()

def callback(msg):
    print(msg.data)
    cahnge_data = 'min : '+str(msg.data)  # string type data
    Twist_data.linear.x = (msg.data%5)-2
    Twist_data.angular.z = msg.data%10
    
    pub.publish(cahnge_data)
    pub2.publish(Twist_data)

rospy.init_node('topic_subscriber')  # subscribe from publisher
sub = rospy.Subscriber('counter', Int32, callback)
pub = rospy.Publisher('min_topic', String, queue_size=1)
pub2 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

# Passive
rospy.spin()