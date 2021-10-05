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
        plane_path = os.path.join(self.storage_path, 'read_rosbag', 'plane_'+str(goal.id))
        print(plane_path)
        cmd_elasticfusion = ["ElasticFusion",  "-l", "plane_3.klg", "-p", "tf.txt", "-cal", "camera_EF.cfg", "d", "2", "-c", "15", "-cv", "1e-01", "-ie", "1e-05", "-pt", "60", "-q", "-name", "scene"]
        ef = subprocess.Popen(cmd_elasticfusion,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(ef.wait())
        print(ef.poll())
        #rosbag.kill()
        print('Finished')
        self.server.set_succeeded()
if __name__ == '__main__':
  rospy.init_node('elastic_fusion_ros')
  server = ElasticFusionROS()
  print('ElasticFusionROS Action Server is ready')
  rospy.spin()
