
import pybullet as p
import numpy as np



# consider a camera; record the images; analysis the image to capture necessary 6D object pose or 6D grasp pose 

class IntelCamera():

    def __init__(self, videoname):

        # positioning the camera 

        #p.resetDebugVisualizerCamera(cameraDistance=0.20, cameraYaw=10, cameraPitch=-30, cameraTargetPosition=[-0.4,-0.35,0.0])
        
        # to look from the top use the following:
        #p.resetDebugVisualizerCamera(cameraDistance=1.20, cameraYaw=30, cameraPitch=-90, cameraTargetPosition=[-0.6,0.0,0.0])

        p.resetDebugVisualizerCamera(cameraDistance=1.20, cameraYaw=20, cameraPitch=-30, cameraTargetPosition=[-0.6,0.0,0.0])
        self.videoname = videoname


    def video(self):
        pass
        # to record a video from this camera uncomment this line
        #p.startStateLogging(p.STATE_LOGGING_VIDEO_MP4, "~/Repositories/KinovaPyBullet/Movies/"+self.videoname+".MP4")
        
    def render(self):
        pass  









