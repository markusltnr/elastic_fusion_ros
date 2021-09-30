#!/usr/bin/env python
import actionlib
import rospy
from std_srvs.srv import Empty, EmptyRequest
import numpy as np
import subprocess
import os
from elastic_fusion_ros.msg import ElasticFusionAction

class ElasticFusionROS:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('elastic_fusion_ros', ElasticFusionAction, self.execute, False)
        self.server.start()
        self.storage_path = '/root/share/'

    def execute(self, goal):
        plane_path = os.path.join(self.rosbag_path, 'read_rosbag', 'plane_'+str(goal.id))
        print(plane_path)
        #cmd_rosbag = ['rosbag', 'record','-b','0','-O', rosbag_filename,'/hsrb/head_rgbd_sensor/rgb/image_raw', '/hsrb/head_rgbd_sensor/depth_registered/image_raw','/tf','/tf_static','/hsrb/head_rgbd_sensor/rgb/camera_info',"__name:=my_bag"]
        rosbag = subprocess.Popen(cmd_rosbag,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        rosbag.kill()
        subprocess.call(["rosnode", "kill", "/my_bag"])
        cmd_move = ['mv', rosbag_filename, self.storage_path]
        move = subprocess.Popen(cmd_move, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.server.set_succeeded()
if __name__ == '__main__':
  rospy.init_node('elastic_fusion_ros')
  server = ElasticFusionROS()
  print('ElasticFusionROS Action Server is ready')
  rospy.spin()
