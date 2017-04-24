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
from time import sleep
import pynter
import pygame
import cv2


def playsound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


def checkperforedcard():


    try:
        camera = FakeCamPymientoCamera('tarjeta2.jpg')

        capture = camera.tomarfoto('pymiento')
        camera.release()
        perfcard = PerforedCard(capture)
        mask = perfcard.getcalculednumberfromholes()
        ok = True
    except PymientoNoBlobsException as e:
        print(" Error: {0}".format(e.message))
        mask = '0000000000000000000000000'
        ok = False
    if ok:
        playsound('electronicping.wav')
    salida = pynter.pinta_cuadro(mask)
    salida.save(mask+'.jpg')
    return mask+'.jpg'

if __name__ == '__main__':
    cv2.namedWindow("pymiento", cv2.WINDOW_NORMAL)
    sindet=cv2.imread('sinDeteccion.png',cv2.IMREAD_COLOR)
    cv2.imshow("pymiento",sindet)
    while True:
        fimage=checkperforedcard()
        img= cv2.imread(filename=fimage,flags=cv2.IMREAD_COLOR)
        cv2.imshow("pymiento",img)
        cv2.waitKey(3000)
