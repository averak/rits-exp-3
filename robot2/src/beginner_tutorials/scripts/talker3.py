#!/usr/bin/env python
import rospy
from std_msgs.msg import String


last_message: str = ""


def callback(data):
    if data.data != last_message:
        print(f"\n[received]: {data.data}")


def talker():
    global last_message

    pub = rospy.Publisher('chatter', String, queue_size=10)
    _ = rospy.Subscriber('chatter', String, callback)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        message = input("[keyinput]: ")
        last_message = message
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
