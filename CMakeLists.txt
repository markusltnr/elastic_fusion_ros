cmake_minimum_required(VERSION 2.9)
project(elastic_fusion_ros)

find_package(catkin REQUIRED  
rospy
std_msgs
actionlib_msgs
message_generation
)

## Generate actions in the 'action' folder
 add_action_files(
   DIRECTORY action
   FILES
   ElasticFusion.action
 )
## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs  
   actionlib_msgs
 )

catkin_package( CATKIN_DEPENDS actionlib_msgs std_msgs message_runtime )
include_directories()
