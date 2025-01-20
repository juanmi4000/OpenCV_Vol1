# Importación de las librerías
from Lib_opencv_vol1.Opencv_vol1 import imagenes as img
from Lib_opencv_vol1.Opencv_vol1 import BLUE, GREEN, RED
import sys
import os

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
# 4. Comprobar si antes de guardar la imagen ya existe (Realizado) (Opencv sobreescribe la imagen si existe. En este caso nos viene bien pero en otra ocasión tengo que tener cuidado)
# 5. Hacer que formatear ruta acepte varios directorios
# 6. Documentar el código
# 7. Importar como librería solo las funciones necesarias (Realizado)
# 8. Comprobar que la imagen no sea None

if menu_consola == 0:
    img.mostrar_menu(imagen, debug)

elif menu_consola == 1:
    #############################################################################
    # Ejercicio 1 (Realizado)
    imangen_generada = img.rotar_180_deg(imagen, debug)
    img.mostrar_imagen(imangen_generada)

    #############################################################################
    # Ejercicio 2 (Realizado)
    # imagen_generada = img.invertir_colores(imagen, debug)
    # img.mostrar_imagen(imagen_generada)


    #############################################################################
    # Ejercicio 3 (Realizado)
    # imangen_generada = img.imagen_gris(imagen, debug)
    # img.mostrar_imagen(imangen_generada)

    #############################################################################
    # Ejercicio 4 (Realizado)
    # punto1 = (1500, 250)
    # punto2 = (2000, 800)
    # imagen_generada = img.dibujar_cuadrado(imagen, punto1, punto2, RED, debug)
    # img.mostrar_imagen(imagen_generada)


    #############################################################################
    # Ejercicio 5 (Realizado)
    # punto1 = (400, 500)
    # punto2 = (500, 600)
    # imagen_generada = img.invertir_color_cuadrado(imagen, punto1, punto2, debug)
    # img.mostrar_imagen(imagen_generada)


    #############################################################################
    # Ejercicio 6 (Realizado)
    # imagen_generada = img.recortar_img_impares(imagen, debug)
    # img.mostrar_imagen(imagen_generada)


    #############################################################################
    # Ejercicio 7 (Realizado)
    # imagen_generada = img.imagen_espejo(imagen, debug)
    # img.mostrar_imagen(imagen_generada)


    #############################################################################
    # Ejercicio 8 (Realizado)
    #imagen_generada = img.invertir_mitad_izquierda_unir_derecha(imagen, debug)
    #img.mostrar_imagen(imagen_generada)



    #############################################################################
    # Ejercicio 9 (Realizado)
    # imagen_generada = img.invertir_mitad_superior_unir_inferior(imagen, debug)
    # img.mostrar_imagen(imagen_generada)


    #############################################################################
    # Ejercicio 10 (Realizado)
    # img.generar_html(imagen, debug)


    #############################################################################
    # Ejercicio 11 (Realizado)
    # punto1 = (1500, 250)
    # punto2 = (2000, 800)
    # imagen_generada = img.dibujar_cuadrado_texto(imagen, punto1, punto2, "Paca", RED, debug)
    # img.mostrar_imagen(imagen_generada)


    #############################################################################
    # Ejercicio 12 (Realizado)
    # punto1 = (1500, 250)
    # punto2 = (2000, 800)
    # imagen_generada = img.emborronar_cuadrado(imagen,punto1, punto2,debug)
    # img.mostrar_imagen(imagen_generada)

    #############################################################################
    # Ejercicio 13
    # imagen_generada = img.detectar_marcar_cara(imagen, RED, debug)
    # img.mostrar_imagen(imagen_generada)

    #############################################################################
    # Ejercicio 14 (Realizado)
    # img.captura_marca_cara_ojos(BLUE, GREEN)

    #############################################################################
    # Ejercicio 15 (Realizado)
    # img.captura_emborronar()


else: 
    print("Lo siento, los valores posibles son 0 para el menú o 1 para consola")