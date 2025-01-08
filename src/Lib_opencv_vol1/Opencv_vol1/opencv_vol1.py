## EDICIÓN Y CAPTURA DE IMÁGENES CON PYTHON Y LA LIBRERÍA OPENCV

## La librería OpenCV para Python da soporte al desarrollo de aplicaciones de visión artificial, nosotros la utilizaremos para practicar con Python e ir creando nuestra propia librería de funciones para la manipulación de ficheros, algunas de estas funciones nos serán muy útiles cuando trabajamos con las APIs de reconocimiento de imágenes.

# Importación de librerías
import cv2
import os


def mostrar_imagen(nombre_imagen: str):
    dir_imagen = obtener_dir(nombre_imagen)
    if dir_imagen != False:
        imagen = cv2.imread(formatear_ruta(dir_imagen, nombre_imagen))
        cv2.imshow("Imagen", imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("La imagen no existe")

# Comprueba que si la imagen exite en la carpeta imagenes o creadas. Por lo contrario devuelve False
def obtener_dir(nombre_imagen: str) -> str | bool:
    return "imagenes" if existe_ruta("imagenes", nombre_imagen) else "creadas" if existe_ruta("creadas", nombre_imagen) else False

# Genero la ruta según el sistema operativo. El directorio puede ser imagenes o creadas y un nombre de la imagen.
def formatear_ruta(directorio: str, nombre_imagen: str) -> str:
    return os.path.join(directorio, nombre_imagen)

# Compruebo si existe una imagen
def existe_ruta(directorio: str, nombre_imagen: str)-> bool:
    return os.path.exists(formatear_ruta(directorio, nombre_imagen))

# Muestra mensaje si la variable debug es True
def mostrar_debug(texto: str, debug: bool):
    if debug:
        print(texto)

# Guarda la imagen en la carpeta creadas
def guardar_imagen(nombre_imagen:str, imagen: str, guardar: bool):
    if guardar:
        # La guardamos en memoria en un fichero distinto y devolvemos la ruta
        cv2.imwrite(formatear_ruta("creadas", nombre_imagen), imagen)
        print("Imagen guardada en el directorio creadas")
    else: 
        print("La imagen generada no se va a guardar")

# Formatea el nombre de la imagen añadiendole un texto identificativo
def formatear_nombre_imagen(nombre_imagen: str, texto: str) -> str:
    return f"{nombre_imagen.split(".")[0]}{texto}{nombre_imagen.split(".")[1]}"


## Se proponen los siguientes ejercicios, que formarán parte de la librería imagenes.py:

#############################################################################
## 1) Crea una función que pasándole la ruta de una imagen, la rote 180 grados y genere una nueva imagen.
def rotar_180_deg(ruta_imagen):
    pass


#############################################################################
## 2) Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir de ella con los colores invertidos


#############################################################################
## 3) Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir ella pero en escala de grises.
def imagen_gris(nombre_imagen :str, guardar=False, debug=False):
    # Cargamos la imagen en memoria
    imagen = cv2.imread(nombre_imagen.lower(), cv2.IMREAD_UNCHANGED)

    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    nombre_nueva_imagen = formatear_nombre_imagen(nombre_imagen, "_gris")
    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, grises, guardar)
    return nombre_nueva_imagen

#############################################################################
## 4) Crea una función que pasándole la ruta de una imagen, marque un cuadrado a partir de dos coordenadas.
## Nota: esta función no reconoce el rostro, se le han pasado las coordenadas del marco como parámetros.


#############################################################################
## 5) Crea una función que pasándole la ruta de una imagen, invierta los colores de un cuadrado a partir de dos coordenadas, pasadas por parámetro.
## Nota: se debe generar una imagen igual pero con los clores invertidos en un determinado cuadrado de la imagen.


#############################################################################
## 6) Crea una función que pasándole la ruta de una imagen, la recorte para evitar dimensiones con valores impares


#############################################################################
## 7) Crea una función que pasándole la ruta de una imagen, retorne la imagen espejada.


#############################################################################
## 8) Crea una función que pasándole la ruta de una imagen, invierte la mitad izquierda y la copie en la derecha.


#############################################################################
## 9) Crea una función que pasándole la ruta de una imagen, invierta la mitad superior y la copie en la inferior, efecto espejo por la horizontal.

#############################################################################
## 10) Crea una función que pasándole la ruta de una imagen, genere un documento html donde muestre la imagen original y las generadas en las tres funciones anteriores en una tabla.


#############################################################################
## 11) Crea una función que pasándole la ruta de una imagen, además de marcar un cuadrado a partir de dos coordenadas, como hizo en el ejercicio4, añada un texto en la parte inferior del cuadrado.
## Nota: Al igual que en el ejercicio 4, realmente no se está detectando caras, se están pasando las coordenadas del marco a la función, además de la imagen y el texto.


#############################################################################
## 12) Crea una función que pasándole la ruta de una imagen, emborrane una zona determinada.
## Nota: para emborronar se ha utilizado la función medianBlur con un tamaño de kernel muy alto.


#############################################################################
## 13) Ahora si. Crea una función que pasándole la ruta de una imagen, detecte y marque las caras de dicha imagen utilizando la funcionalidad de CV2. Esta librería posisibilita la detección de objetos mediante aprendizaje automático en cascada. Podemos entrenar nuestros propios clasificadores, pero para este ejercicio utilizaremos un clasificador preentrenado que puedes encontrar en el GitHub de OpenCV (opencv/data/haarcascades/).
