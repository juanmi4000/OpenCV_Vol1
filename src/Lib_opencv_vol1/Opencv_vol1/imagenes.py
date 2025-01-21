## EDICIÓN Y CAPTURA DE IMÁGENES CON PYTHON Y LA LIBRERÍA OPENCV

## La librería OpenCV para Python da soporte al desarrollo de aplicaciones de visión artificial, nosotros la utilizaremos para practicar con Python e ir creando nuestra propia librería de funciones para la manipulación de ficheros, algunas de estas funciones nos serán muy útiles cuando trabajamos con las APIs de reconocimiento de imágenes.

## --> Enunciados

# --> Mis comentarios

# Importación de librerías
import cv2
import os
import webbrowser
from typing import Tuple, List
import numpy as np
import screeninfo as si

BLUE = [255, 0, 0]
GREEN = [0, 255, 0]
RED = [0, 0, 255]


def mostrar_imagen(nombre_imagen: str):
    """
    Muestra una imagen y la ajusta a la pantalla según su tamaño.

    Args:
        nombre_imagen (str): Nombre de la imagen de entrada.

    """

    imagen = cv2.imread(nombre_imagen)

    alto, ancho = imagen.shape[:2]

    monitores = si.get_monitors()

    alto_monitor, ancho_monitor = monitores[0].height, monitores[0].width

    if alto > alto_monitor or ancho > ancho_monitor:
        escala_ancho = ancho_monitor / ancho
        escala_alto = alto_monitor / alto
        escala = min(escala_ancho, escala_alto)
        nuevo_ancho = int(ancho * escala)
        nuevo_alto = int(alto * escala)
        imagen = cv2.resize(imagen, (nuevo_ancho, nuevo_alto), interpolation=cv2.INTER_AREA)
    


    cv2.imshow("Imagen", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def formatear_ruta(directorios: List, nombre_imagen: str) -> str:
    """
    Formatea la ruta de la imagen.

    Args:
        directorios (List): Lista con los directorios donde se encuentra la imagen.

    Returns:
        np.ndarray: Imagen procesada (arreglo de NumPy).
    """
    return os.path.join(*directorios, nombre_imagen)


def mostrar_debug(texto: str, debug: bool):
    """
    Muestra un mensaje en pantalla si el modo debug está activado. 

    Args:
        texto (str): Mensaje a mostrar.
        debug (bool): Modo debug activado o desactivado.
    """
    if debug:
        print(texto)

def guardar_imagen(nombre_imagen: str, imagen: np.ndarray):
    """
    Guarda una imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): Nombre con el que se guardará la imagen, incluyendo su extensión.
        imagen (np.ndarray): Imagen que se desea guardar.

    Returns:
        None
    """
    cv2.imwrite(nombre_imagen, imagen)
    print("Imagen guardada en el directorio creadas")

def pedir_color() -> Tuple[int, int, int] | bool:
    """
    Solicita al usuario que seleccione un color entre rojo, verde y azul.

    Returns:
        Tuple[int, int, int]: Tupla que representa el color seleccionado (BGR).
        bool: Retorna False si el usuario selecciona una opción inválida.
    """
    opcion = int(input("Elige un color:\n\t1. Rojo\n\t2. Verde\n\t3. Azul\n"))
    return (255, 0, 0) if opcion == 1 else (0, 255, 0) if opcion == 2 else (0, 0, 255) if opcion == 3 else False

def pedir_punto() -> Tuple[int, int]:
    """
    Solicita al usuario ingresar las coordenadas de un punto.

    Returns:
        Tuple[int, int]: Coordenadas del punto ingresado (x, y).
    """
    x = int(input("Introduce el valor de la x: "))
    y = int(input("Introduce el valor de la y: "))
    return (x, y)

def formatear_nombre_imagen(nombre_imagen: str, texto: str) -> str:
    """
    Formatea el nombre de una imagen agregando un texto adicional antes de la extensión.

    Args:
        nombre_imagen (str): Nombre original de la imagen, incluyendo su extensión.
        texto (str): Texto que se agregará al nombre de la imagen.

    Returns:
        str: Nombre formateado de la imagen.
    """
    return f"{nombre_imagen.split('.')[0]}{texto}.{nombre_imagen.split('.')[1]}"

def mostrar_menu(nombre_imagen: str, debug: bool) -> any:
    """
    Muestra un menú principal para interactuar con el usuario.

    Args:
        nombre_imagen (str): Nombre de la imagen seleccionada.
        debug (bool): Modo de depuración.

    Returns:
        any: Retorna el resultado de la función `ejecutar_opcion`.
    """
    print("BIENVENIDO A LOS EJERCICIOS DE OPENCV VOLUMEN 1")
    print(f"La imagen elegida es {nombre_imagen}")
    
    opcion = int(input(menu()))
    return ejecutar_opcion(opcion, nombre_imagen, debug)

def ordenar_puntos(punto1: Tuple[int, int], punto2: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Ordena dos puntos dados para que estén en orden ascendente por sus coordenadas.

    Args:
        punto1 (Tuple[int, int]): Primer punto (x1, y1).
        punto2 (Tuple[int, int]): Segundo punto (x2, y2).

    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]]: Puntos ordenados en formato ((x1, y1), (x2, y2)).
    """
    x1, x2 = min(punto1[0], punto2[0]), max(punto1[0], punto2[0])
    y1, y2 = min(punto1[1], punto2[1]), max(punto1[1], punto2[1])
    return ((x1, y1), (x2, y2))

def ejecutar_opcion(opcion: int, imagen: str, debug: bool) -> any:
    """
    Realiza los pasos a seguir según una opción.

    Args:
        opcion (int): Opción elegida.
        imagen (str): Nombre de la imagen.
        debug (bool): Modo de depuración.

    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]]: Puntos ordenados en formato ((x1, y1), (x2, y2)).
    """
    if opcion == 1:
        imangen_generada = rotar_180_deg(imagen, debug)
        mostrar_imagen(imangen_generada)
    elif opcion == 2:
        imagen_generada = invertir_colores(imagen, debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 3:
        imangen_generada = imagen_gris(imagen, debug)
        mostrar_imagen(imangen_generada)
    elif opcion == 4:
        color = pedir_color()
        if not color:
            while not color:
                print("Color no válidao, escoja un color válido")
                color = pedir_color()
        print("Primero introducimos el punto inferior izquierdo: ")
        punto1 = pedir_punto()
        print("Ahora introducimos el punto superior derecho: ")
        punto2 = pedir_punto()
        imagen_generada = dibujar_cuadrado(imagen, punto1, punto2, color, debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 5:
        print("Primero introducimos el punto inferior izquierdo: ")
        punto1 = pedir_punto()
        print("Ahora introducimos el punto superior derecho: ")
        punto2 = pedir_punto()
        imagen_generada = invertir_color_cuadrado(imagen, punto1, punto2, color, debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 6:
        imagen_generada = recortar_img_impares(imagen, debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 7:
        imagen_generada = imagen_espejo(imagen, debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 8:
        imagen_generada = invertir_mitad_izquierda_unir_derecha(imagen, debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 9:
        imagen_generada = invertir_mitad_superior_unir_inferior(imagen, debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 10:
        generar_html(imagen, debug)
    elif opcion == 11:
        imagen_generada = dibujar_cuadrado_texto(imagen, debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 12:
        print("Primero introducimos el punto inferior izquierdo: ")
        punto1 = pedir_punto()
        print("Ahora introducimos el punto superior derecho: ")
        punto2 = pedir_punto()
        imagen_generada = emborronar_cuadrado(imagen,punto1, punto2,debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 13:
        imagen_generada = detectar_marcar_cara(imagen, RED, debug)
        mostrar_imagen(imagen_generada)
    elif opcion == 14:
        captura_marca_cara_ojos()
    elif opcion == 15:
        captura_emborronar()


def menu() -> str: 
    """
    Muestra el menú de las opciones que se pueden hacer con las imagenes.

    Returns:
        str: Cadena con las opciones.
    """
    return """
    ¿Qué desea hacer con la imagen?
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
        13. Marcar cuadrado caras con clasificador
        14. Abrir webcam y marcar caras y ojos
        15. Abrir webcam y emborronar caras
    
    Elige un opción de 1 a 12: """

def leer_imagen(nombre_imagen: str) -> np.ndarray:
    """
    Lee una imagen y comprueba que exista.

    Args:
        nombre_imagen (str): Nombre de la imagen de entrada.

    Returns:
        np.ndarray: Imagen procesada.
    """
    imagen = cv2.imread(formatear_ruta(["imagenes"], nombre_imagen), cv2.IMREAD_UNCHANGED)
    if imagen is None:
        raise FileNotFoundError(f"El nombre de la imagen {nombre_imagen} no se encuentra en el directorio imágenes.")
    return imagen


## Se proponen los siguientes ejercicios, que formarán parte de la librería imagenes.py:

#############################################################################
## 1) Crea una función que pasándole la ruta de una imagen, la rote 180 grados y genere una nueva imagen.
def rotar_180_deg(nombre_imagen: str, debug: bool = False) -> str:
    """
    Rota una imagen 180 grados y guarda la imagen rotada en una nueva ruta en el directorio imagenes/creadas..

    Args:
        nombre_imagen (str): La ruta de la imagen a rotar.
        debug (bool, optional): Si es True, se mostrarán mensajes de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen rotada 180 grados.
    """
    imagen = leer_imagen(nombre_imagen)
    img_rotada = cv2.rotate(imagen, cv2.ROTATE_180)

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_rotada_180"))

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen rotada 180 grados: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, img_rotada)

    return nombre_nueva_imagen




#############################################################################
## 2) Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir de ella con los colores invertidos
def invertir_colores(nombre_imagen: str, debug: bool = False) -> str:
    """
    Invierte los colores de una imagen y guarda la nueva imagen con los colores invertidos en el directorio imagenes/creadas..

    Args:
        nombre_imagen (str): El nombre del archivo de la imagen a procesar.
        debug (bool, optional): Si es True, se mostrarán mensajes de depuración. Por defecto es False.

    Returns:
        str: El nombre del archivo de la nueva imagen con los colores invertidos.
    """
    imagen = leer_imagen(nombre_imagen)

    img_colores_invertidos = cv2.bitwise_not(imagen)

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_invertir_colores")) 
    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, img_colores_invertidos)
    return nombre_nueva_imagen


#############################################################################
## 3) Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir ella pero en escala de grises.
def imagen_gris(nombre_imagen :str, debug: bool = False) -> str:
    """
    Convierte una imagen a escala de grises y guarda la nueva imagen en el directorio imagenes/creadas..
    
    Args:
        nombre_imagen (str): El nombre del archivo de la imagen a convertir.
        debug (bool, optional): Si es True, se imprimirá información de depuración. Por defecto es False.
    
    Returns:
        str: El nombre del nuevo archivo de imagen en escala de grises.
    """
    
    imagen = leer_imagen(nombre_imagen)

    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_gris"))
    
    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, grises)
    return nombre_nueva_imagen

#############################################################################
## 4) Crea una función que pasándole la ruta de una imagen, marque un cuadrado a partir de dos coordenadas.
## Nota: esta función no reconoce el rostro, se le han pasado las coordenadas del marco como parámetros.
def dibujar_cuadrado(nombre_imagen: str, punto1: Tuple[int, int], punto2: Tuple[int, int], color: Tuple[int, int, int] = (255, 0, 0), debug: bool = False,) -> str:
    """
    Dibuja un rectángulo en una imagen y guarda la nueva imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        punto1 (Tuple[int, int]): La esquina superior izquierda del rectángulo.
        punto2 (Tuple[int, int]): La esquina inferior derecha del rectángulo.
        color (Tuple[int, int, int], optional): El color del rectángulo en formato BGR. Por defecto es (255, 0, 0).
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen con el rectángulo dibujado.
    """
    imagen = leer_imagen(nombre_imagen)

    (x1, y1), (x2, y2) = ordenar_puntos(punto1, punto2)

    cuadrado = cv2.rectangle(imagen, (x1, y1), (x2, y2), color, 4)

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_cuadrado"))

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, cuadrado)

    return nombre_nueva_imagen

#############################################################################
## 5) Crea una función que pasándole la ruta de una imagen, invierta los colores de un cuadrado a partir de dos coordenadas, pasadas por parámetro.
## Nota: se debe generar una imagen igual pero con los clores invertidos en un determinado cuadrado de la imagen.
def invertir_color_cuadrado(nombre_imagen: str, punto1: Tuple[int, int], punto2: Tuple[int, int], debug: bool = False) -> str:
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

    parte_invertida = imagen[y1:y2, x1:x2]

    imagen[y1:y2, x1:x2] = cv2.bitwise_not(parte_invertida)

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_cuadrado_invertido"))

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, imagen)

    
    return nombre_nueva_imagen

#############################################################################
## 6) Crea una función que pasándole la ruta de una imagen, la recorte para evitar dimensiones con valores impares
def recortar_img_impares(nombre_imagen: str, debug: bool = False) -> str:
    """
    Recorta la imagen si sus dimensines son impares y guarda la nueva imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen recortada las dimensiones.
    """
    imagen = leer_imagen(nombre_imagen)
    
    alto, ancho = imagen.shape[:2]

    if alto % 2 != 0:
        alto -= 1
    if ancho % 2 != 0:
        ancho -= 1

    imagen_recortada = imagen[:alto, :ancho]

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_dim_par"))

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con los colores en escala de grises llamada: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, imagen_recortada)

    return nombre_nueva_imagen

#############################################################################
## 7) Crea una función que pasándole la ruta de una imagen, retorne la imagen espejada.
def imagen_espejo(nombre_imagen: str, debug: bool = False) -> str:
    """
    Imagen espejo a partir de una imagen inicial y guarda la nueva imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen espejo.
    """
    imagen = leer_imagen(nombre_imagen)
    
    # 0: Reflejo vertical (de arriba hacia abajo).
    # 1: Reflejo horizontal (de izquierda a derecha, como un espejo).
    # -1: Reflejo en ambas direcciones (horizontal y vertical).

    imagen_espejo = cv2.flip(imagen, 1)

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_espejo"))

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen espejo: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, imagen_espejo)

    return nombre_nueva_imagen

#############################################################################
## 8) Crea una función que pasándole la ruta de una imagen, invierte la mitad izquierda y la copie en la derecha.
def invertir_mitad_izquierda_unir_derecha(nombre_imagen: str, debug: bool = False) -> str:
    """
    A parir de una imagen, invierte la mitad izquierda, la une a la parte derecha y guarda la nueva imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen.
    """
    imagen = leer_imagen(nombre_imagen)

    alto, ancho = imagen.shape[:2]

    if alto % 2 != 0:
        alto -= 1
    if ancho % 2 != 0:
        ancho -= 1

    mitad_izquierda_invertida = cv2.flip(imagen[:alto, :int(ancho/2)], 1)

    imagen[:alto, int(ancho/2):ancho] = mitad_izquierda_invertida

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_espejo_mitad_izquierdo_copie_derecho"))

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen invertida por la mitad izquierda y copiada en la derecha: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, imagen)

    return nombre_nueva_imagen

#############################################################################
## 9) Crea una función que pasándole la ruta de una imagen, invierta la mitad superior y la copie en la inferior, efecto espejo por la horizontal.
def invertir_mitad_superior_unir_inferior(nombre_imagen: str, debug: bool = False) -> str:
    """
    A parir de una imagen, invierte la mitad superior, la une a la parte inferior y guarda la nueva imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen.
    """
    imagen = leer_imagen(nombre_imagen)

    alto, ancho = imagen.shape[:2]

    if alto % 2 != 0:
        alto -= 1
    if ancho % 2 != 0:
        ancho -= 1

    mitad_superior_invertida = cv2.flip(imagen[:int(alto/2), :ancho], 0)

    imagen[int(alto/2):alto, :ancho] = mitad_superior_invertida

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_espejo_mitad_superior_copie_inferior"))

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen invertida por la mitad izquierda y copiada en la derecha: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, imagen)
    
    return nombre_nueva_imagen


#############################################################################
## 10) Crea una función que pasándole la ruta de una imagen, genere un documento html donde muestre la imagen original y las generadas en las tres funciones anteriores en una tabla.
def generar_html(nombre_imagen: str, debug: bool = False):
    """
    Genera un HTML con la imagen original, su espejo, su mitad izquierda unida a la derecha, su mitad superior unida en la parte inferior y genera el html y lo abre en un navegador.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.
    """
    leer_imagen(nombre_imagen)
    
    img_ejercicio_7 = imagen_espejo(nombre_imagen, debug)
    img_ejercicio_8 = invertir_mitad_izquierda_unir_derecha(nombre_imagen, debug)
    img_ejercicio_9 = invertir_mitad_superior_unir_inferior(nombre_imagen, debug)

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Comparativa de funciones espejo</title>
        <style>
            ul {{
                list-style: none;
                width: 70%;
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                grid-template-rows: repeat(2, 1fr);
                gap: 20px;
                margin: 0 auto;
            }}

            img{{
                width: 400px;
            }}
        </style>
    </head>
    <body>
        <ul>
            <li>
                <p>Imagen Original: {formatear_ruta(["imagenes"], nombre_imagen)}</p>
                <img src="{os.path.join(os.getcwd(), formatear_ruta(["imagenes"], nombre_imagen))}" alt="Imagen original">
            </li>
            <li>
                <p>Imagen Espejada: {img_ejercicio_7}</p>
                <img src="{os.path.join(os.getcwd(), img_ejercicio_7)}" alt="Imagen Espejada">
            </li>
            <li>
                <p>Imagen Doblada Verticalmente: {img_ejercicio_8}</p>
                <img src="{os.path.join(os.getcwd(), img_ejercicio_8)}" alt="Imagen Doblada Verticalmente">
            </li>
            <li>
                <p>Imagen Doblada Horizontalmente: {img_ejercicio_9}</p>
                <img src="{os.path.join(os.getcwd(), img_ejercicio_9)}" alt="Imagen Doblada Horizontalmente">
            </li>
        </ul>
    </body>
    </html>
    """

    nombre_html = os.path.join("html", "html_generado.html")

    with open(nombre_html, "w", encoding="UTF-8") as html_archivo:
        html_archivo.write(html)

    webbrowser.open(f"file://{os.path.join(os.getcwd(), nombre_html)}")
    # print(os.getcwd()) # Me da la ruta en la que encuentro en la terminal


#############################################################################
## 11) Crea una función que pasándole la ruta de una imagen, además de marcar un cuadrado a partir de dos coordenadas, como hizo en el ejercicio4, añada un texto en la parte inferior del cuadrado.
## Nota: Al igual que en el ejercicio 4, realmente no se está detectando caras, se están pasando las coordenadas del marco a la función, además de la imagen y el texto.
def dibujar_cuadrado_texto(nombre_imagen: str, punto1: Tuple[int, int], punto2: Tuple[int, int], texto: str, color: Tuple[int, int, int] = (0, 0, 255), debug: bool = False,) -> str:
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

    cuadrado = cv2.rectangle(imagen, (x1, y1), (x2, y2), color, 4)

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_cuadrado_texto"))
    font = cv2.FONT_HERSHEY_SIMPLEX

    texto_pos = (punto1[0] + 20, punto2[1] - 10)

    cv2.putText(imagen, texto, texto_pos, font, 4, color, 2, cv2.LINE_AA)

    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con un cuadrado según unas coordenadas y un texto: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, cuadrado)

    return nombre_nueva_imagen


#############################################################################
## 12) Crea una función que pasándole la ruta de una imagen, emborrane una zona determinada.
## Nota: para emborronar se ha utilizado la función medianBlur con un tamaño de kernel muy alto.
def emborronar_cuadrado(nombre_imagen: str, punto1: Tuple[int, int], punto2: Tuple[int, int], debug: bool = False) -> str:
    """
    A parir de una imagen emborrona un rectángulo y guarda la nueva imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        punto1 (Tuple[int, int]): La esquina superior izquierda del rectángulo.
        punto2 (Tuple[int, int]): La esquina inferior derecha del rectángulo.
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen con un rectangulo emborronado.
    """
    imagen = leer_imagen(nombre_imagen)

    zona_borrosa = imagen[punto1[1]:punto2[1], punto1[0]:punto2[0]]

    img_emborronada =  cv2.medianBlur(zona_borrosa, 99)

    imagen[punto1[1]:punto2[1], punto1[0]:punto2[0]] = img_emborronada

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_cuadrado_emborronado"))
    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con un cuadrado según unas coordenadas y un texto: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, imagen)

    return nombre_nueva_imagen

#############################################################################
## 13) Ahora si. Crea una función que pasándole la ruta de una imagen, detecte y marque las caras de dicha imagen utilizando la funcionalidad de CV2. Esta librería posisibilita la detección de objetos mediante aprendizaje automático en cascada. Podemos entrenar nuestros propios clasificadores, pero para este ejercicio utilizaremos un clasificador preentrenado que puedes encontrar en el GitHub de OpenCV (opencv/data/haarcascades/).
def detectar_marcar_cara(nombre_imagen: str, color: Tuple[int, int, int], debug: bool = False) -> str:
    """
    A parir de una imagen y un clasificador, detecta una cara para luego marcarla y guarda la nueva imagen en el directorio imagenes/creadas.

    Args:
        nombre_imagen (str): La ruta de la imagen original.
        color (Tuple[int, int, int]): El color del rectángulo en formato BGR.
        debug (bool, optional): Si es True, imprime información de depuración. Por defecto es False.

    Returns:
        str: La ruta de la nueva imagen con la cara marcada por un rectángulo.
    """
    imagen = leer_imagen(nombre_imagen)

    modelo_cara = cv2.CascadeClassifier("clasificadores/haarcascade_frontalface_default.xml")

    # Lo procesa mejor ya que no tiene información de colores
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # devuelve las diferentes caras
    caras = modelo_cara.detectMultiScale(imagen_gris, 1.3, 5)

    for (x, y, w, h) in caras:
        cv2.rectangle(imagen, (x, y), (x + w, y + h), color, 4)

    nombre_nueva_imagen = formatear_ruta(["imagenes", "creadas"], formatear_nombre_imagen(nombre_imagen, "_cuadrado_clasificador"))
    mostrar_debug(f"A partir de la imagen: {imagen}", debug)
    mostrar_debug(f"Se generará la imagen con un cuadrado según unas coordenadas que nos da el clasificador: {nombre_nueva_imagen}", debug)

    guardar_imagen(nombre_nueva_imagen, imagen)

    return nombre_nueva_imagen



#############################################################################
## 14) Crea una función que realice capturas con la webcam y marque cara y ojos del rostro.
def captura_marca_cara_ojos(color_cara: Tuple[int, int, int], color_ojos: Tuple[int, int, int]):
    """
    Abre la webcam y marca con un rectangulo la cara y los ojos.

    Args:
        color_cara (Tuple[int, int, int]): El color del rectángulo de la cara en formato BGR.
        color_ojos (Tuple[int, int, int]): El color del rectángulo de los ojos en formato BGR.
    """
    modelo_cara = cv2.CascadeClassifier("clasificadores/haarcascade_frontalface_default.xml")
    modelo_ojos = cv2.CascadeClassifier("clasificadores/haarcascade_eye.xml")
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
                for (ex, ey, ew, eh) in ojos:
                    cv2.rectangle(region_color, (ex, ey), (ex + ew, ey + eh), color_ojos, 2)
            cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

#############################################################################
## 15) Crea una función que realice una captura con la webcam, como en el ejercicio anterior, pero que esta vez, en lugar de marcarla, la emborrone.
def captura_emborronar():
    """
    Abre la webcam y emborrona las caras.
    """
    modelo_cara = cv2.CascadeClassifier("clasificadores/haarcascade_frontalface_default.xml")
    video = cv2.VideoCapture(0)
    while video.isOpened():
        ret, frame = video.read()
        if frame is not None:
            gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            caras = modelo_cara.detectMultiScale(gris, 1.3, 5)
            for (x, y, w, h) in caras:
                zona_borrosa = frame[y:y + h, x:x + w]
                zona_borrosa = cv2.medianBlur(zona_borrosa, 99)
                frame[y:y + h, x:x + w] = zona_borrosa
            cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
