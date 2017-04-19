'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-

Pymiento Project (C) 2017

Autor: Victor Suarez 

PymientoExceptions: Fichero con las excepciones

Usa OpenCV.

Version 2.0.0.20170419
'''


class PymientoException(Exception):
    def __init__(self, message='Hay ocurrido un Pyerror.'):
        self.message=message

pass


class PymientoNoBlobsException(PymientoException):

    def __init__(self, message='No se detecta tarjeta....'):
        self.message=message

pass