# Importación de las librerías
from Lib_opencv_vol1 import Opencv_vol1 as cv_vol1
import sys
import os

# print(sys.argv) # Muestra todos los argumentos pasados por consola

imagen = sys.argv[1].lower()
# debug = True if len(sys.argv) > 2 else False
debug = False

# cv_vol1.mostrar_imagen(imagen)
# cv_vol1.mostrar_menu(imagen)


#############################################################################
# Ejercicio 1
imangen_generada = cv_vol1.rotar_180_deg(imagen, debug)
cv_vol1.mostrar_imagen(imangen_generada)

#############################################################################
# Ejercicio 2


#############################################################################
# Ejercicio 3
# imangen_generada = cv_vol1.imagen_gris(imagen, debug)
# cv_vol1.mostrar_imagen(imangen_generada)

#############################################################################
# Ejercicio 4


#############################################################################
# Ejercicio 5


#############################################################################
# Ejercicio 6


#############################################################################
# Ejercicio 7


#############################################################################
# Ejercicio 8


#############################################################################
# Ejercicio 9


#############################################################################
# Ejercicio 10


#############################################################################
# Ejercicio 12


#############################################################################
# Ejercicio 13


