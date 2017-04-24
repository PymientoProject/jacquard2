# Configuracion red wifi:
	
	* Abrir el terminal y poner la sentencia "wpa_gui"
	
# Descarga de sonidos .wav

	* Visitar la pagina http://www.freespecialeffects.co.uk
	* Escoger el sonido que nos guste 
	* Descargarlo a la carpeta del pymiento con una  sentencia como esta de ejemplo
	" sudo wget http://www.freespecialeffects.co.uk/soundfx/scifi/electronicping.wav"
	
* Iniciar el programa automáticamente cuando se arranca la Raspberry

 El siguiente es un método sencillo, testeado y depurable para hacer arranques 
 de programas en el inicio.

 Crea en el escritorio un archivo .desktop con el nombre por ejemplo “pymiento.desktop”

 Escribe lo siguiente en el archivo :

 [Desktop Entry]
 Encoding=UTF-8
 Type=Application
 Name= Pymiento
 Comment=
 Exec= sudo python /home/pi/Pymiento/detectorTarjeta.py
 StartupNotify=false
 Terminal=true
 Hidden=false


 Dos cosas importantes respecto a nuestro programa, 
 ha de estar marcado como ejecutable y si hace uso de rutas de archivos en su código, 
 dichas rutas han de estar en forma absoluta y no relativa.

 Ahora , al pinchar dos veces sobre archivo .desktop del escritorio nos debe lanzar la aplicación,
 esto es útil ya que nos permite ver si hay algún problema con el lanzamiento antes de hacerlo 
 automático en el arrranque .

 Para que dicha aplicación se lance al inicio hay que copiar el archivo en el directorio
 “ /home/pi/.config/autostart/”  (creándolo si no existe), y ya está.

 Para que dicha aplicación no se lance al principio basta con quitar el lanzador 
 de la carpeta autostart
 

	
