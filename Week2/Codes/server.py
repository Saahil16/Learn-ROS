#!/usr/bin/env python3

from math import pi
import rospy
from geometry_msgs.msg import Twist
from code.srv import polygon_s, polygon_sResponse

class polygon_server:
    
    def __init__(self):
        rospy.init_node('draw_server')
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(1)  
        self.velocity = Twist()
        self.polygon = rospy.Service('draw', polygon_s, self.draw) 




    def draw(self, req):
        angle = 2 * pi / req.n
        duration = 1
        for _ in range(req.n):
            t0 = rospy.Time.now().to_sec()
            while rospy.Time.now().to_sec() - t0 <= duration:
                self.velocity.angular.z = angle
                self.pub.publish(self.velocity)
                
                
            self.velocity.angular.z = 0
            self.pub.publish(self.velocity)
            t0 = rospy.Time.now().to_sec()
            
            while rospy.Time.now().to_sec() - t0 <= duration:
                self.velocity.linear.x = 2
                self.pub.publish(self.velocity)
                
                
                
            self.velocity.linear.x = 0
            self.pub.publish(self.velocity)
            
        return polygon_sResponse(success=True)

if __name__ == '__main__':
    try:
        controller = polygon_server()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
