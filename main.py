'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-

Pymiento Project (C) 2017

Autor: Victor Suarez 

Main: Deteccion de tarjeta perforada y generacion de dibujo

Usa OpenCV.

Version 2.0.0.20170419
'''


from PymientoCamera import WebcamPymientoCamera,FakeCamPymientoCamera
from PerforedCard import PerforedCard
from PymientoExceptions import PymientoNoBlobsException
import pynter
#import pygame
import cv2

'''def playsound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
'''
Ok = True
cv2.namedWindow('pymiento',cv2.WINDOW_AUTOSIZE)
while(True):
    try:
        camera = FakeCamPymientoCamera('temp.jpg')

        capture = camera.tomarfoto('pymiento')
        camera.release()
        perfcard = PerforedCard(capture)
        mask = perfcard.getcalculednumberfromholes()
        Ok = True
    except PymientoNoBlobsException as e:
        print(" Error: {0}".format(e.message))
        mask = '0000000000000000000000000'
        Ok = False
    '''if Ok:
        playsound('electronicping.wav')'''
    salida = pynter.pinta_cuadro(mask)
    salida.save(mask+'.jpg')
    imgsalida = cv2.imread(mask+'.jpg',cv2.IMREAD_UNCHANGED)
    cv2.imshow('pymiento',imgsalida)
    

