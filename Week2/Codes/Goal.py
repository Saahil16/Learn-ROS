#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt, pow

class TurtleController:
    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)

        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)

        self.pose = Pose()
        self.rate = rospy.Rate(5)

    def pose_callback(self, data):
        self.pose = data

    def move_turtle(self, target_x, target_y):
        while not rospy.is_shutdown():
            vel_msg = Twist()

            distance = sqrt(pow(target_x - self.pose.x, 2) + pow(target_y - self.pose.y, 2))
            angle = atan2(target_y - self.pose.y, target_x - self.pose.x)

            vel_msg.linear.x = 1.0 * sqrt(pow(target_x - self.pose.x, 2) + pow(target_y - self.pose.y, 2))
            vel_msg.angular.z = 4.0 * (angle - self.pose.theta)

            self.velocity_publisher.publish(vel_msg)
            print(f"Current Position: x={self.pose.x:.2f}, y={self.pose.y:.2f}, theta={self.pose.theta:.2f}")

            if distance < 0.01:
                break

            self.rate.sleep()

if __name__ == '__main__':
    try:
        controller = TurtleController()
        target_x = float(input("Enter target x-coordinate: "))
        target_y = float(input("Enter target y-coordinate: "))
        controller.move_turtle(target_x, target_y)
    except rospy.ROSInterruptException:
        pass
