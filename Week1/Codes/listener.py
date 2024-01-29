#!/usr/bin/env python3

import rospy
from code.msg import MyCustomMsg

def callback(data):
    rospy.loginfo("Received: %s", data)


def subsrciber():
    rospy.init_node('subsrciber', anonymous=True)
    rospy.Subscriber('custom_topic', MyCustomMsg, callback)
    rospy.spin()


if __name__ == '__main__':
    subsrciber()
