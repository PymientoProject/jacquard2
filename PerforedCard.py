'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-

Pymiento Project (C) 2017

Autor: Victor Suarez 

PerforedCard: Calculo del numero a partir de la deteccion.

Usa OpenCV.

Version 2.0.0.20170419
'''
from BlobDetector import PymientoBlobDetector
from PymientoExceptions import PymientoNoBlobsException
from math import pi
import cv2

class PerforedCard:
    detector = None
    _mask='0000000000000000000000000'
    def __init__(self, filename):
        self.detector=PymientoBlobDetector(filename)

    def calcularAreaBlob(self,blob):
        return pi* (blob.size/2)**2

    def calcularposicion(self,blob,mask):

        #calculo de la y
        coordx, coordy = blob.pt
        if coordy<=40:
            posy=0
        elif coordy>40 and coordy<=127:
            posy=1
        elif coordy>127 and coordy<=207:
            posy=2
        elif coordy>207 and coordy<=353:
            posy=3
        elif coordy>353 and coordy<=430:
            posy=4
        else:
            posy=0

        #calculo de la x


        if coordx in range(0,30):
            posx=0
        elif coordx in range(30,110):
            posx=1
        elif coordx in range(110,190):
            posx=2
        elif coordx in range(190,280):
            posx=3
        elif coordx in range(280,370):
            posx=4
        elif coordx in range(370,450):
            posx = 4
        else:
            posx=0

        mask[posy*6+posx] = '1'
        return mask

    def getcalculednumberfromholes(self):

        blobs = self.detector.detect_blobs()
        currentmask= '%s' % self._mask
        lcurrentmask= list(currentmask)
        if len(blobs) <= 0 :
            raise PymientoNoBlobsException()
        elif len(blobs) == 1 and self.calcularAreaBlob(blobs[0]) > 1900: #area agujero por defecto
            raise PymientoNoBlobsException(message='Error, La deteccion es erronea')
        else:
            for blob in blobs:
                lcurrentmask=self.calcularposicion(blob,lcurrentmask)

            return "".join(lcurrentmask)

pass