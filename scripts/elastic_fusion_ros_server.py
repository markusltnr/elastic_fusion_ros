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
        klg_file = os.path.join(plane_path, 'plane_'+str(goal.id)+'.klg')
        trajectories_file = os.path.join(plane_path, 'planes', 'tf.txt')
        camera_cfg_file = os.path.join(self.storage_path, 'camera_EF.cfg')
        output_file = os.path.join(self.storage_path, 'scene_'+str(goal.id))
        #cmd_elasticfusion = ["ElasticFusion",  "-l", klg_file, "-cal", camera_cfg_file, "d", "2", "-c", "15", "-cv", "1e-01", "-ie", "1e-05", "-pt", "60", "-f", "-q", "-name", output_file]
        cmd_elasticfusion = ["ElasticFusion",  "-l", klg_file, "-cal", camera_cfg_file]
        cmd_elasticfusion.extend(rospy.get_param('/elasticfusion/call_params', ["-d", "2", "-c", "15", "-cv", "1e-01", "-ie", "1e-05", "-pt", "60", "-f", "-q"]))
        cmd_elasticfusion.extend(["-name", output_file])
        print(cmd_elasticfusion)
        
        ef = subprocess.Popen(cmd_elasticfusion)#,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ef.wait()
        self.server.set_succeeded()
if __name__ == '__main__':
  rospy.init_node('elastic_fusion_ros')
  server = ElasticFusionROS()
  print('ElasticFusionROS Action Server is ready')
  rospy.spin()
