# Importación de las librerías
from Lib_opencv_vol1 import Opencv_vol1 as cv_vol1
import sys
import os

BLUE = [255, 0, 0]
GREEN = [0, 255, 0]
RED = [0, 0, 255]

# print(sys.argv) # Muestra todos los argumentos pasados por consola

imagen = sys.argv[1].lower()
menu_consola = int(sys.argv[2]) if len(sys.argv) >= 3 else 1
debug = sys.argv[3] if len(sys.argv) >= 4 else False


# Argumentos que le tenemos que pasar al script:
# Explicación: python main.py nombre_imagen.jgp (0 - menú o 1 - consola) (mostrar los debug)
# Ejemplo: python main.py f1.jpg 1 False

# Mejoras:
# 1. Que te lo muestre según la pantalla. (Realizado)
# 2. Realizar una pequeña guía sobre los argumentos que le paso (Realizado)
# 3. Comprobar que los debug estén bien escritos (Realizado, le dejo en valor por defecto para que siempre esté en falso)
# 4. Comprobar si antes de guardar la imagen ya existe
# 5. Hacer que formatear ruta acepte varios directorios
# 6. Documentar el código
# 7. Importar como librería solo las funciones necesarias

if menu_consola == 0:
    cv_vol1.mostrar_menu(imagen, debug)

elif menu_consola == 1:
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
    # Ejercicio 12 (Realizado)
    # punto1 = (1500, 250)
    # punto2 = (2000, 800)
    # imagen_generada = cv_vol1.emborronar_cuadrado(imagen,punto1, punto2,debug)
    # cv_vol1.mostrar_imagen(imagen_generada)

    #############i################################################################
    # Ejercicio 13


    #############################################################################
    # Ejercicio 14
    cv_vol1.captura_marca_cara_ojos()

    #############################################################################
    # Ejercicio 15


else: 
    print("Lo siento, los valores posibles son 0 para el menú o 1 para consola")