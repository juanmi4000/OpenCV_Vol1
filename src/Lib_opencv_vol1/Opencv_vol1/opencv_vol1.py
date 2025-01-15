## EDICIÓN Y CAPTURA DE IMÁGENES CON PYTHON Y LA LIBRERÍA OPENCV

## La librería OpenCV para Python da soporte al desarrollo de aplicaciones de visión artificial, nosotros la utilizaremos para practicar con Python e ir creando nuestra propia librería de funciones para la manipulación de ficheros, algunas de estas funciones nos serán muy útiles cuando trabajamos con las APIs de reconocimiento de imágenes.

# Importación de librerías
import cv2
import os


def mostrar_imagen(nombre_imagen: str):
    # hacer que se ajuste a la pantalla
    imagen = cv2.imread(nombre_imagen)
    cv2.imshow("Imagen", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Genero la ruta según el sistema operativo. El directorio puede ser imagenes o creadas y un nombre de la imagen.
def formatear_ruta(directorio: str, nombre_imagen: str) -> str:
    # Debería de pasarle una lista
    return os.path.join(directorio, nombre_imagen)

# Debería de comprobar que la imagen existe

# Muestra mensaje si la variable debug es True
def mostrar_debug(texto: str, debug: bool):
    if debug:
        print(texto)

# Guarda la imagen en el directorio "creadas"
"""
def menu_guardar_imagen(nombre_imagen:str, imagen: str, guardar: bool):
    if guardar:
        guardar_imagen(nombre_imagen, imagen)
    else: 
        opcion = "no"
        while len(opcion) > 1:
            opcion = input("¿Está seguro que no quiere guardar la imagen? [S/N]").lower()
            if opcion == "S":
                print("La imagen generada no se va a guardar")
            else:
                guardar_imagen(nombre_imagen, imagen)
"""

def guardar_imagen(nombre_imagen:str, imagen: str):
    cv2.imwrite(nombre_imagen, imagen)
    print("Imagen guardada en el directorio creadas")

# Formatea el nombre de la imagen añadiendole un texto identificativo
def formatear_nombre_imagen(nombre_imagen: str, texto: str) -> str:
    return f"{nombre_imagen.split(".")[0]}{texto}.{nombre_imagen.split(".")[1]}"

def mostrar_menu(nombre_imagen: str) -> any:
    print("BIENVENIDO A LOS EJERCICIOS DE OPENCV VOLUMEN 1")

    print(f"La imagen elegida es {nombre_imagen}")

    # Comprobar que se un número
    opcion = int(input(menu()))
    ejecutar_opcion(opcion)
    

def ejecutar_opcion(opcion: int):
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    elif opcion == 7:
        pass
    elif opcion == 8:
        pass
    elif opcion == 9:
        pass
    elif opcion == 10:
        pass
    elif opcion == 11:
        pass
    elif opcion == 12:
        pass

def menu() -> str: 
    return """
    ¿Qué desea hacer con la imagén?
        1. Girar 180º
        2. Invertir colores
        3. Escala de grises
        4. Mostrar cuadrado a partir de dos coordenadas
        5. Invertir colores en un cuadrado
        6. Recortar imagen para obtener valores pares
        7. Obtener la imagen espejo
        8. Invertir mitad izquierda y copiar en la derecha
        9. Invertir mitad superior y copiar en la inferior
        10. Generar HTML con la imagen original y las tres anteriores
        11. Mostrar un cuadrado y un nombre
        12. Enborronar imagen en un zona determinada
    
    Elige un opción de 1 a 12: 
    """




## Se proponen los siguientes ejercicios, que formarán parte de la librería imagenes.py:

#############################################################################
## 1) Crea una función que pasándole la ruta de una imagen, la rote 180 grados y genere una nueva imagen.
def rotar_180_deg(nombre_imagen: str, debug: bool = False) -> str:
    imagen = cv2.imread(formatear_ruta("imagenes", nombre_imagen), cv2.IMREAD_UNCHANGED)

    img_rotada = cv2.rotate(imagen, cv2.ROTATE_180)

    nombre_nueva_imagen = formatear_ruta("imagenes/creadas", formatear_nombre_imagen(nombre_imagen, "_rotada_180"))

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, img_rotada)
    return nombre_nueva_imagen




#############################################################################
## 2) Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir de ella con los colores invertidos
def invertir_colores(nombre_imagen: str, debug: bool = False) -> str:
    imagen = cv2.imread(formatear_ruta("imagenes", nombre_imagen), cv2.IMREAD_UNCHAGED)

    img_colores_invertidos = "Poner aquí el método"

    nombre_nueva_imagen = formatear_nombre_imagen(nombre_imagen, "_invertir_colores")
    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, img_colores_invertidos)
    return nombre_nueva_imagen


#############################################################################
## 3) Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir ella pero en escala de grises.
def imagen_gris(nombre_imagen :str, debug: bool = False) -> str:
    # Cargamos la imagen en memoria
    imagen = cv2.imread(formatear_ruta("imagenes", nombre_imagen), cv2.IMREAD_UNCHANGED)

    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    nombre_nueva_imagen = formatear_ruta("imagenes/creadas", formatear_nombre_imagen(nombre_imagen, "_gris"))
    
    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, grises)
    return nombre_nueva_imagen

#############################################################################
## 4) Crea una función que pasándole la ruta de una imagen, marque un cuadrado a partir de dos coordenadas.
## Nota: esta función no reconoce el rostro, se le han pasado las coordenadas del marco como parámetros.
def dibujar_cuadrado(nombre_imagen: str, debug: bool = False) -> str:
    return ""

#############################################################################
## 5) Crea una función que pasándole la ruta de una imagen, invierta los colores de un cuadrado a partir de dos coordenadas, pasadas por parámetro.
## Nota: se debe generar una imagen igual pero con los clores invertidos en un determinado cuadrado de la imagen.
def invertir_color_cuadrado(nombre_imagen: str, debug: bool = False) -> str:
    return ""

#############################################################################
## 6) Crea una función que pasándole la ruta de una imagen, la recorte para evitar dimensiones con valores impares
def recortar_img_impares(nombre_imagen: str, debug: bool = False) -> str:
    return ""

#############################################################################
## 7) Crea una función que pasándole la ruta de una imagen, retorne la imagen espejada.
def imagen_espejo(nombre_imagen: str, debug: bool = False) -> str:
    return ""

#############################################################################
## 8) Crea una función que pasándole la ruta de una imagen, invierte la mitad izquierda y la copie en la derecha.
def invertir_mitad_izquierda_unir_derecha(nombre_imagen: str, debug: bool = False) -> str:
    return ""

#############################################################################
## 9) Crea una función que pasándole la ruta de una imagen, invierta la mitad superior y la copie en la inferior, efecto espejo por la horizontal.
def invertir_mitad_superior_unir_inferior(nombre_imagen: str, debug: bool = False) -> str:
    return ""


#############################################################################
## 10) Crea una función que pasándole la ruta de una imagen, genere un documento html donde muestre la imagen original y las generadas en las tres funciones anteriores en una tabla.
def generar_html(nombre_imagen: str, debug: bool = False) -> str:
    return ""


#############################################################################
## 11) Crea una función que pasándole la ruta de una imagen, además de marcar un cuadrado a partir de dos coordenadas, como hizo en el ejercicio4, añada un texto en la parte inferior del cuadrado.
## Nota: Al igual que en el ejercicio 4, realmente no se está detectando caras, se están pasando las coordenadas del marco a la función, además de la imagen y el texto.
def dibujar_cuadrado_texto (nombre_imagen: str, debug: bool = False) -> str:
    return ""


#############################################################################
## 12) Crea una función que pasándole la ruta de una imagen, emborrane una zona determinada.
## Nota: para emborronar se ha utilizado la función medianBlur con un tamaño de kernel muy alto.
def emborronar_cuadrado(nombre_imagen: str, debug: bool = False) -> str:
    return ""

#############################################################################
## 13) Ahora si. Crea una función que pasándole la ruta de una imagen, detecte y marque las caras de dicha imagen utilizando la funcionalidad de CV2. Esta librería posisibilita la detección de objetos mediante aprendizaje automático en cascada. Podemos entrenar nuestros propios clasificadores, pero para este ejercicio utilizaremos un clasificador preentrenado que puedes encontrar en el GitHub de OpenCV (opencv/data/haarcascades/).



#############################################################################
## 14) Crea una función que realice capturas con la webcam y marque cara y ojos del rostro.



#############################################################################
## 15) Crea una función que realice una captura con la webcam, como en el ejercicio anterior, pero que esta vez, en lugar de marcarla, la emborrone.



