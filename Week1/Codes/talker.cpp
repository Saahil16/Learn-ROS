// talker.cpp
#include "ros/ros.h"
#include "code/MyCustomMsg.h"

int main(int argc, char **argv)
{


  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher cuspub=n.advertise<code::MyCustomMsg>("custom_topic", 10);

  ros::Rate loop_rate(10);



  while (ros::ok())
  {
    code::MyCustomMsg msg;
    msg.my_int=2402;
    msg.my_str="It finally works";
    msg.my_bool=true;




    ROS_INFO("Publishing: %d, %s, %s",msg.my_int,msg.my_str.c_str(),msg.my_bool ? "true" : "false");
    cuspub.publish(msg);
    ros::spinOnce();


    loop_rate.sleep();
  }

  return 0;
}
