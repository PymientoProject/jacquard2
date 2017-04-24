# jacquard2
jacquard version 2.0 OpenCV

Versión 2 del programa Jacquard2 el cual permite a partir de una tarjeta perforada generar unas imagenes. En esta nueva versión se ha modificado la detección delos agujeros de la librería Simple CV por Opencv.
Ademas se ha hecho una refactorización del código para que sea más legible.

Para más info consultar la anterior [versión](https://github.com/PymientoProject/Jacquard).

Novedades de esta versión:

Este proyecto, tiene 2 ramas. La rama principal o master, que contiene la versión compatible con python 2.7; además de
los siguientes requisitos.

* pygame 1.9.3 -> Solo para Python 2.7; no añadir en Python 3.x.
* pillow 4.1.0
* Opencv 2.4.3


_NOTA_: Se ha añadido un fichero requeriments.txt para ayudar a la instalación de las dependencias. Para instalarlo con
PIP:

```bash
$ pip install -r requeriments.txt
```

Como funciona:

Para ejecutar el programa, simplemente ejecutar:

```bash
$ python main.py
```

Según esta creado este proyecto se permiten utilizar distintas camaras ya sea en la propia RAspberry o una webcam. Para
cambiar del tipo de camara, observar las clases dentro del fichero _pymientoCamera.py_ en el cual hay 4 clases:

* _PymientoCamera_: Clase abastracta que no se puede utilizar se debe usar para implementar nuevas camras.
* _WebcamPymientoCamera_: Clase que permite utilizar una camara web de un ordenador de escritorio (o webcam por USB).
* _FakeCamPymientoCamera_: Clase que implementa una camara falsa. Sirve como depuración ya que siempre devolvera el mismo
fichero.
* _PiCameraPymientoCamera_: Clase que implementa la camara de la Raspberry Pi. **NOTA**: Esta clase viene comentada;
descomentar tanto la clase como el import para usar en Raspberry Pi.


## Compatibilidad con Python3 y opencv3.

Para poder crear la versión compatible con opencv3 y python 3, se debe utilizar la rama llamada _python3_ la cual
configurará el proyecto y librerías para este entorno.

## Configuración para arrancar la Raspberry Pi con el programa.

Ver archivo configuración.md