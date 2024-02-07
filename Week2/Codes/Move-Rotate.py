#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import curses

class turtlecontrol:
    def __init__(self):
        rospy.init_node('turtle_keyboard_control', anonymous=True)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        self.vel_x = 1.0
        self.z = 1.0

        self.velocity = Twist()
    def key_inputs(self, stdscr):
        stdscr.clear()
        stdscr.refresh()
        return stdscr.getch()

    def keystart(self, stdscr):
        while not rospy.is_shutdown():
            key = self.key_inputs(stdscr)
            self.move(key)
        
    def move(self, key):
        if key == curses.KEY_UP:
            self.velocity.linear.x = self.vel_x
            self.velocity.angular.z = 0
        elif key == curses.KEY_DOWN:
            self.velocity.linear.x = - self.vel_x
            self.velocity.angular.z = 0
        elif key == curses.KEY_LEFT:
            self.velocity.angular.z = self.z
            self.velocity.linear.x = 0
        elif key == curses.KEY_RIGHT:
            self.velocity.angular.z = -self.z
            self.velocity.linear.x = 0
        self.pub.publish(self.velocity)    
         
  
if __name__ == '__main__':
    try:
        Turtle_control = turtlecontrol()
        curses.wrapper(Turtle_control.keystart)
        
    except rospy.ROSInterruptException:
        pass
