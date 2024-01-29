// listener.cpp
#include "ros/ros.h"
#include "code/MyCustomMsg.h"

void callback(const code::MyCustomMsg::ConstPtr& msg)
{
  ROS_INFO("Received: %d, %s, %s",msg->my_int,msg->my_str.c_str(),msg->my_bool ? "true" : "false");
}
int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");
  ros::NodeHandle n;

  ros::Subscriber cussub=n.subscribe("custom_topic", 10, callback);
  ros::spin();

  return 0;
}
