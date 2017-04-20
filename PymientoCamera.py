'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-

Pymiento Project (C) 2017

Autor: Victor Suarez 

PymientoCamera: Control de las camaras

Usa OpenCV.

Version 2.0.0.20170419
'''

from abc import ABCMeta,abstractmethod
from string import ascii_uppercase
import random
import cv2


class PymientoCamera:
    __metaclass__ = ABCMeta

    @abstractmethod
    def tomarfoto(self,filename_prefix):  pass

    def generaterandomname(self, len=6):
        return ''.join(random.choice(ascii_uppercase) for _ in range(len))

    @abstractmethod
    def release(self):  pass

pass


class WebcamPymientoCamera(PymientoCamera):

    cameraport=None
    camera = None
    width = 2592
    height = 1944
    brigthness = 50

    def __init__(self, cameraport=0):
        self.cameraport = cameraport
        self.camera = cv2.VideoCapture(cameraport)
        self.camera.set(cv.CV_CAP_PROP_FRAME_WIDTH, self.width)
        self.camera.set(cv.CV_CAP_PROP_FRAME_HEIGHT, self.height)
        self.camera.set(cv.CV_CAP_PROP_BRIGHTNESS, self.brigthness)

    def tomarfoto(self,filename_prefix):
        retval, img = self.camera.read()
        filename= filename_prefix+self.generaterandomname()+'.jpg'
        cv2.imwrite(filename=filename, img=img)
        return filename

    def release(self):
        self.camera.release()
pass


class FakeCamPymientoCamera(PymientoCamera):
    filename=None

    def __init__(self,filename):
        self.filename=filename

    def tomarfoto(self,filename_prefix):
        return self.filename

    def release(self):
        return
pass
