#!/usr/bin/env python3
import sys
import rospy
from code.srv import polygon_s

def polygon_client(n):
    rospy.wait_for_service('draw')
    try:
        polygon = rospy.ServiceProxy('draw', polygon_s)
        x=polygon(n)
    except rospy.ServiceException as e:
        print("Failed: %s"%e)

if __name__ == "__main__":
    n = int(sys.argv[1])
    polygon_client(n)
    print("Requesting n= %f"%(n))