# Importación de las librerías
from Lib_opencv_vol1 import Opencv_vol1 as cv_vol1
import sys
import os

BLUE = [255, 0, 0]
GREEN = [0, 255, 0]
RED = [0, 0, 255]

# print(sys.argv) # Muestra todos los argumentos pasados por consola

imagen = sys.argv[1].lower()
# debug = True if len(sys.argv) > 2 else False
debug = False


# cv_vol1.mostrar_menu(imagen, debug)


# Mejoras:
# 1. Que te lo muestre según la pantalla.
# 2. Realizar una pequeña guía sonre los argumentos que le paso
# 3. Comprobar que los debug estén bien escritos
# 4. Comprobar si antes de guardar la imagen ya existe
# 5. Hacer que formatear ruta acepte varios directorios
# 6. Documentar el código

#############################################################################
# Ejercicio 1 (Realizado)
# imangen_generada = cv_vol1.rotar_180_deg(imagen, debug)
# cv_vol1.mostrar_imagen(imangen_generada)

#############################################################################
# Ejercicio 2 (Realizado)
# imagen_generada = cv_vol1.invertir_colores(imagen, debug)
# cv_vol1.mostrar_imagen(imagen_generada)


#############################################################################
# Ejercicio 3 (Realizado)
# imangen_generada = cv_vol1.imagen_gris(imagen, debug)
# cv_vol1.mostrar_imagen(imangen_generada)

#############################################################################
# Ejercicio 4 (Realizado)
# punto1 = (1500, 250)
# punto2 = (2000, 800)
# imagen_generada = cv_vol1.dibujar_cuadrado(imagen, punto1, punto2, RED, debug)
# cv_vol1.mostrar_imagen(imagen_generada)


#############################################################################
# Ejercicio 5 (Realizado)
# punto1 = (400, 500)
# punto2 = (500, 600)
# imagen_generada = cv_vol1.invertir_color_cuadrado(imagen, punto1, punto2, debug)
# cv_vol1.mostrar_imagen(imagen_generada)


#############################################################################
# Ejercicio 6 (Realizado)
# imagen_generada = cv_vol1.recortar_img_impares(imagen, debug)
# cv_vol1.mostrar_imagen(imagen_generada)


#############################################################################
# Ejercicio 7 (Realizado)
# imagen_generada = cv_vol1.imagen_espejo(imagen, debug)
# cv_vol1.mostrar_imagen(imagen_generada)


#############################################################################
# Ejercicio 8 (Realizado)
#imagen_generada = cv_vol1.invertir_mitad_izquierda_unir_derecha(imagen, debug)
#cv_vol1.mostrar_imagen(imagen_generada)



#############################################################################
# Ejercicio 9 (Realizado)
# imagen_generada = cv_vol1.invertir_mitad_superior_unir_inferior(imagen, debug)
# cv_vol1.mostrar_imagen(imagen_generada)


#############################################################################
# Ejercicio 10 (Realizado)
# cv_vol1.generar_html(imagen, debug)


#############################################################################
# Ejercicio 11 (Realizado)
# punto1 = (1500, 250)
# punto2 = (2000, 800)
# imagen_generada = cv_vol1.dibujar_cuadrado_texto(imagen, punto1, punto2, "Paca", RED, debug)
# cv_vol1.mostrar_imagen(imagen_generada)


#############################################################################
# Ejercicio 12
# imagen_generada = cv_vol1.emborronar_cuadrado(imagen, debug)


#############################################################################
# Ejercicio 13


#############################################################################
# Ejercicio 14


#############################################################################
# Ejercicio 15


