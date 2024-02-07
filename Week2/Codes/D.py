#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class Draw:
    def __init__(self):
        rospy.init_node('turtle_draw_d', anonymous=True)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.velocity = Twist()
        self.rate = rospy.Rate(1) 

    def pose_callback(self, pose):
        pass

    def move(self, linear_vel, angular_vel, duration):
        self.velocity.linear.x = linear_vel
        self.velocity.angular.z = angular_vel
        self.pub.publish(self.velocity)
        rospy.sleep(duration)
   
        self.velocity.linear.x = 0
        self.velocity.angular.z = 0
        self.pub.publish(self.velocity)

    
    def draw_d(self):
        rospy.sleep(1.0)
        self.move(0.0,-1.5,2.0)
        rospy.sleep(1.0)
        self.move(1.5, 0.0, 2.0)
        rospy.sleep(1.0)

        self.move(0.0, 1.0, 1.5)
        rospy.sleep(1.5)

        self.move(2.0, 3.0, 4.0)
        rospy.sleep(0)
        self.move(2.0,3.0,0.3)      

if __name__ == '__main__':
    try:
        turtle_drawing = Draw()
        turtle_drawing.draw_d()
    except rospy.ROSInterruptException:
        pass
