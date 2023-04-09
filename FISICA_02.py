import os
import cv2
import csv
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

# Configurar ruta al archivo de video
video_file = 'video.mp4'

# Configurar ruta a la carpeta para guardar los fotogramas
frames_folder = 'frames'

# Configurar tiempo inicial y contador de fotogramas
start_time = 0
frame_count = 0

# Abrir archivo de video
cap = cv2.VideoCapture(video_file)

# Crear carpeta para guardar los fotogramas
if not os.path.exists(frames_folder):
    os.makedirs(frames_folder)

# Iterar a través de los fotogramas del video
while True:
    ret, frame = cap.read()
    if ret:
        # Obtener tiempo actual del video
        current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

        # Si ha pasado al menos 2 segundos desde el último fotograma guardado
        if current_time - start_time >= 2:
            # Guardar fotograma como archivo de imagen
            cv2.imwrite(os.path.join(frames_folder, 'frame_{}.jpg'.format(frame_count)), frame)
            
            # Actualizar tiempo y contador de fotogramas
            start_time = current_time
            frame_count += 1
    else:
        break

# Cerrar archivo de video
cap.release()

# Crear la carpeta "recortes_vel" si no existe
if not os.path.exists('recortes_vel'):
    os.makedirs('recortes_vel')

# Definir las coordenadas de los recuadros a recortar
recuadros = [(1090, 600, 1205, 685)]

# Recortar los recuadros de todas las imágenes
for i in range(0, 88):
    # Cargar la imagen
    ruta_imagenes = 'frames/'
    imagen = Image.open(ruta_imagenes + f'frame_{i}.jpg')
    
    # Recortar los recuadros y guardarlos en la carpeta "recortes_vel"
    for j, recuadro in enumerate(recuadros):
        recorte = imagen.crop(recuadro)
        recorte.save(f'recortes_vel/frame_{i}_recorte{j+1}.jpg')

# Crear la carpeta "recortes_tiempo" si no existe
if not os.path.exists('recortes_tiempo'):
    os.makedirs('recortes_tiempo')

# Definir las coordenadas de los recuadros a recortar
recuadros = [(1555, 990, 1860, 1045)]

# Recortar los recuadros de todas las imágenes
for i in range(0, 88):
    # Cargar la imagen
    ruta_imagenes = 'frames/'
    imagen = Image.open(ruta_imagenes + f'frame_{i}.jpg')
    
    # Recortar los recuadros y guardarlos en la carpeta "recortes_tiempo"
    for j, recuadro in enumerate(recuadros):
        recorte = imagen.crop(recuadro)
        recorte.save(f'recortes_tiempo/frame_{i}_recorte{j+1}.jpg')

# Se abre el archivo CSV en modo de escritura
archivo_csv = open('datos.csv', 'w', newline='')
writer = csv.writer(archivo_csv)

# Se escriben los encabezados en el archivo CSV
writer.writerow(['Frame', 'Velocidad', 'Tiempo'])

# Se define la ruta de las imágenes y se recorre la secuencia
ruta_imagenes_vel = 'recortes_vel/'
ruta_imagenes_tiempo = 'recortes_tiempo/'
for i in range(0, 87):
    # Se carga la imagen 1
    imagen_vel = cv2.imread(ruta_imagenes_vel + f'frame_{i}_recorte1.jpg')
        
    # Para que el OCR lo lea mejor...
    
    gray = cv2.cvtColor(imagen_vel, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Remover ruido e invertir imagen
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    
    # Se aplica OCR al recorte1
    velocidad = pytesseract.image_to_string(opening, lang='eng', config='--psm 6')

    # Se carga la imagen 2
    imagen_tiempo = cv2.imread(ruta_imagenes_tiempo + f'frame_{i}_recorte1.jpg')
        
    #  Para que el OCR lo lea mejor...
    
    gray = cv2.cvtColor(imagen_tiempo, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Remover ruido e invertir imagene
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    
    # Se aplica OCR al recorte2
    tiempo = pytesseract.image_to_string(invert)

    # Se escribe el resultado en el archivo CSV
    writer.writerow([f'frame_{i}.jpg', velocidad, tiempo])

# Se cierra el archivo CSV
archivo_csv.close()