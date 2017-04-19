'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

Pymiento Project (C) 2017

Autor: Victor Suarez 

Blob Detector: Deteccion de Blobs para la tarjeta perforada.

Usa OpenCV.

Version 2.0.0.20170419
'''

import cv2
import numpy as np

from abc import ABCMeta, abstractmethod

# Class BlobDetector: clase base para los detectores( por si se cambia en un futuro).
class BlobDetector:
    __metaclass__ = ABCMeta

    @abstractmethod
    def detect_blobs(self):  pass

    @abstractmethod
    def __init__(self,filename):  pass

pass

class PymientoBlobDetector:

    imagepath=''

    def __init__(self,filename):
        self.imagepath=filename

    def detect_blobs(self):
        # Leemos la imagen de fichero
        image = cv2.imread(self.imagepath,cv2.IMREAD_GRAYSCALE)
        #hacemos que la imagen ocupe 1/3
        imgresized = cv2.resize(image,dsize=(0,0),fx=0.33,fy=0.33)
        #imcroped= imgresized[320:50, 480:500]
        # Detectamos las formas
        detector = cv2.SimpleBlobDetector()

        keypoints = detector.detect(imgresized)

        #im_with_keypoints = cv2.drawKeypoints(imgresized, keypoints, np.array([]), (0, 0, 255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        #cv2.imshow('test',im_with_keypoints)
        #cv2.waitKey(0)
        return keypoints

pass

