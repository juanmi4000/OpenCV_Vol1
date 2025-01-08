## EDICIÓN Y CAPTURA DE IMÁGENES CON PYTHON Y LA LIBRERÍA OPENCV

## La librería OpenCV para Python da soporte al desarrollo de aplicaciones de visión artificial, nosotros la utilizaremos para practicar con Python e ir creando nuestra propia librería de funciones para la manipulación de ficheros, algunas de estas funciones nos serán muy útiles cuando trabajamos con las APIs de reconocimiento de imágenes.

# Importación de librerías
import cv2

## Se proponen los siguientes ejercicios, que formarán parte de la librería imagenes.py:

#############################################################################
## 1) Crea una función que pasándole la ruta de una imagen, la rote 180 grados y genere una nueva imagen.
def rotar_180_deg(ruta_imagen):
    pass


#############################################################################
## 2) Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir de ella con los colores invertidos


#############################################################################
## 3) Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir ella pero en escala de grises.


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
