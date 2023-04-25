import csv
from math import sqrt, atan2, degrees, radians, cos, sin

def calcular_largo(punto_x, punto_y):
    return sqrt(punto_x**2 + punto_y**2)

def calcular_angulo(punto_x, punto_y):
    return degrees(atan2(punto_y, punto_x))

def calcular_vector_desplazamiento(punto_x1, punto_y1, punto_x2, punto_y2):
    desplazamiento_x = punto_x2 - punto_x1
    desplazamiento_y = punto_y2 - punto_y1
    return (desplazamiento_x, desplazamiento_y)

def verificar_punto_x(angulo, radio, punto_x):
    return round(punto_x, 4) == round(radio*cos(radians(angulo)), 4)

def verificar_punto_y(angulo, radio, punto_y):
    return round(punto_y, 4) == round(radio*sin(radians(angulo)), 4)

def verificar_largo_vector_desplazamiento(largo_a, largo_b, angulo_a_b):
    coseno_angulo = cos(radians(angulo_a_b))
    return round(largo_a, 4) == round(sqrt(largo_b**2 + largo_a**2 - 2*largo_b*largo_a*coseno_angulo), 4)


with open('datos.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    data = []
    for row in reader:
        vector_id = int(row[0])
        largo = float(row[1])
        angulo = float(row[2])
        punto_x = float(row[3])
        punto_y = float(row[4])

        # Calculos
        nuevo_row = row
        nuevo_row.append(calcular_largo(punto_x, punto_y))
        nuevo_row.append(calcular_angulo(punto_x, punto_y))

        # Ultima fila de datos para calcular vector de desplazamiento
        if len(data) > 0:
            row_anterior = data[-1]
            punto_x_anterior = float(row_anterior[3])
            punto_y_anterior = float(row_anterior[4])
            desplazamiento = calcular_vector_desplazamiento(punto_x_anterior, punto_y_anterior, punto_x, punto_y)
            nuevo_row += desplazamiento

            # Verificaciones
            largo_anterior = float(row_anterior[5])
            angulo_a_b = angulo - float(row_anterior[2])
            if not verificar_largo_vector_desplazamiento(calcular_largo(*desplazamiento), largo_anterior, angulo_a_b):
                print(f"Error en verificación de largo del vector de desplazamiento en la fila {vector_id}")
            
            if not verificar_punto_x(angulo, calcular_largo(punto_x, punto_y), punto_x):
                print(f"Error en verificación de PUNTO_X en la fila {vector_id}")
            
            if not verificar_punto_y(angulo, calcular_largo(punto_x, punto_y), punto_y):
                print(f"Error en verificación de PUNTO_Y en la fila {vector_id}")
        
        data.append(nuevo_row)


with open('datos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir encabezado actualizado
    header += ['LARGO_CALCULADO', 'ANGULO_CALCULADO', 'DESP_X', 'DESP_Y']
    writer.writerow(header)

    # Escribir filas con datos actualizados
    for row in data:
        writer.writerow(row)
