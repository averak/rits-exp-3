#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(data.data)


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    _ = rospy.Subscriber('chatter', String, callback)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        message = input("[keyinput]: ")
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
