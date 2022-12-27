#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')  # 'topic_publisher'라는 이름으로 로스파이 초기화

pub = rospy.Publisher('counter', Int32, queue_size=10)   # 'counter'라는 이름의 토픽으로 데이터를 생성()
rate = rospy.Rate(10)   # 전송 주기(단위: Hz)
count = 0

while not rospy.is_shutdown():
    pub.publish(count)
    count += 1
    rate.sleep()