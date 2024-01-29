#!/usr/bin/env python3

import rospy
from code.msg import MyCustomMsg

def publisher():
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('custom_topic', MyCustomMsg, queue_size=10)
    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():
        msg = MyCustomMsg()
        msg.my_int = 1632
        msg.my_str = "It works,thank god"
        msg.my_bool = True
        rospy.loginfo("Publishing: %s", msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
