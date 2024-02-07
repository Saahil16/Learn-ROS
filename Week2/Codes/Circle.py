#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class Circle:
    def __init__(self):
        rospy.init_node('draw_circle_node', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.twist_msg = Twist()
        self.rate = rospy.Rate(10)
        self.current_pose = Pose()

    def pose_callback(self, data):
        self.current_pose = data

    def draw_circle(self, radius):
        initial_angle = self.current_pose.theta
        angular_velocity = 1.0  
        linear_velocity = angular_velocity * radius

        while not rospy.is_shutdown():
            current_angle = self.current_pose.theta - initial_angle
            if current_angle >= 2 * math.pi:
                break
            self.twist_msg.linear.x = linear_velocity
            self.twist_msg.angular.z = angular_velocity
            self.cmd_vel_pub.publish(self.twist_msg)
            self.rate.sleep()
            
            
        self.twist_msg.linear.x = 0.0
        self.twist_msg.angular.z = 0.0
        self.cmd_vel_pub.publish(self.twist_msg)

if __name__ == '__main__':
    try:
        draw_circle_node = Circle()
        radius = float(input("Enter the radius of the circle: "))
        draw_circle_node.draw_circle(radius)

    except rospy.ROSInterruptException:
        pass
