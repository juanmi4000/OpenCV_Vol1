#############################################################################
## EJERCICIOS DE AMPLIACIÓN

## Se proponen los siguientes ejercicios de ampliación, que formarán parte de la librería imagenes2.py

# Importaciones 
from .imagenes import leer_imagen, ordenar_puntos, formatear_ruta, formatear_nombre_imagen, mostrar_debug, guardar_imagen
from typing import Tuple
import cv2

#############################################################################
## 5b) Como variante del ejercicio 5 se propone invertir los colores de toda la imagen menos del marco indicado. Añadirlo como funcionalidad extra, es decir, por defecto la función operará como hasta ahora pero podrá pedírsele que realice la operación aquí descrita.
def invertir_color_cuadrado(nombre_imagen: str, punto1: Tuple[int, int], punto2: Tuple[int, int], invertir_resto_imagen: bool, debug: bool = False) -> str:
    """
    Invierte los colores de un rectángulo en una imagen y guarda la nueva imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        punto1 (Tuple[int, int]): La esquina superior izquierda del rectángulo.
        punto2 (Tuple[int, int]): La esquina inferior derecha del rectángulo.
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen con el cuadrado invertido.
    """

    imagen = leer_imagen(nombre_imagen)

    (x1, y1), (x2, y2) = ordenar_puntos(punto1, punto2)

    parte_escogida = imagen[y1:y2, x1:x2]

    if invertir_resto_imagen:
        imagen = cv2.bitwise_not(imagen)
        imagen[y1:y2, x1:x2] = parte_escogida
        nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_img_invertido_menos_cuadrado"))
    else:
        imagen[y1:y2, x1:x2] = cv2.bitwise_not(parte_escogida)
        nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_cuadrado_invertido"))



    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, imagen)

    
    return nombre_nueva_imagen


#############################################################################
## 11b) Como variante del ejercicio 11, se propone transformar toda la imagen fuera del marco a tonos de gris. Añadirlo como funcionalidad extra.

## 11c) Como variante del ejercicio 11, se propone que la imagen generada contenga solo el marco seleccionado. Incluyendo un perímetro en tonos de grises, además la etiqueta podrá estar vacía

## 11d) Como variante del ejercicio 11 se propone que el texto sea opcional y se ajuste al tamaño del cuadrado

# Los tres ejericicios anteriores se van a unificar en uno solo, ya que comparten la misma funcionalidad.
def dibujar_cuadrado_texto(nombre_imagen: str, punto1: Tuple[int, int], punto2: Tuple[int, int], texto: str, gris: bool, recortar: bool, color: Tuple[int, int, int] = (0, 0, 255), debug: bool = False,) -> str:
    """
    Dibuja un rectángulo en una imagen, un texto y guarda la nueva imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        punto1 (Tuple[int, int]): La esquina superior izquierda del rectángulo.
        punto2 (Tuple[int, int]): La esquina inferior derecha del rectángulo.
        color (Tuple[int, int, int], optional): El color del rectángulo en formato BGR. Por defecto es (255, 0, 0).
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen con el rectángulo dibujado y el texto.
    """
    imagen = leer_imagen(nombre_imagen)

    (x1, y1), (x2, y2) = ordenar_puntos(punto1, punto2)

    if gris:
        imagen_original = imagen.copy()

        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imagen_gris = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

        imagen_gris[y1:y2, x1:x2] = imagen_original[y1:y2, x1:x2]

        imagen = imagen_gris

        if recortar:
            imagen = imagen[y1 - 50:y2 + 50, x1 - 50:x2 + 50]
            nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_img_gris_menos_cuadrado_perimetro"))
        else:
            nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_img_gris_menos_cuadrado"))
    else:
        if recortar:
            imagen = imagen[y1 - 30:y2 + 30, x1 - 30:x2 + 30]
            nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_img_cuadrado_texto_perimetro"))
        else:
            nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_img_gris_menos_cuadrado"))

    cuadrado = cv2.rectangle(imagen, (x1, y1), (x2, y2), color, 4)

    font = cv2.FONT_HERSHEY_SIMPLEX

    texto_pos = (punto1[0] + 20, punto2[1] - 10)

    cv2.putText(imagen, texto, texto_pos, font, 4, color, 2, cv2.LINE_AA)

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con un cuadrado según unas coordenadas y un texto: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, cuadrado)

    return nombre_nueva_imagen


#############################################################################
## 14b) Revisa el resto de clasificadores preentrenados de Haar en la ibrería OpenCV para detectar otros elementos. Por ejemplo la boca. Investiga como podrías entrenar tu propio modelo.
def captura_marca_cara_ojos(color_cara: Tuple[int, int, int], color_ojos: Tuple[int, int, int], color_risa:Tuple[int, int, int]):
    """
    Abre la webcam y marca con un rectangulo la cara y los ojos.

    Args:
        color_cara (Tuple[int, int, int]): El color del rectángulo de la cara en formato BGR.
        color_ojos (Tuple[int, int, int]): El color del rectángulo de los ojos en formato BGR.
    """
    modelo_cara = cv2.CascadeClassifier("clasificadores/haarcascade_frontalface_default.xml")
    modelo_ojos = cv2.CascadeClassifier("clasificadores/haarcascade_eye.xml")
    modelo_risa = cv2.CascadeClassifier("clasificadores/haarcascade_smile.xml")
    video = cv2.VideoCapture(0)
    while video.isOpened():
        ret, frame = video.read()
        if frame is not None:
            gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            caras = modelo_cara.detectMultiScale(gris, 1.3, 5)
            for (x, y, w, h) in caras:
                cv2.rectangle(frame, (x, y), (x + w, y + h), color_cara, 2)
                region_gris = gris[y:y + h, x:x + w]
                region_color = frame[y:y + h, x:x + w]
                ojos = modelo_ojos.detectMultiScale(region_gris)
                risas = modelo_risa.detectMultiScale(region_gris)
                for (ex, ey, ew, eh) in ojos:
                    cv2.rectangle(region_color, (ex, ey), (ex + ew, ey + eh), color_ojos, 2)
                for (sx, sy, sw, sh) in risas:
                    cv2.rectangle(region_color, (sx, sy), (sx + sw, sy + sh), color_risa, 2)
            cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()