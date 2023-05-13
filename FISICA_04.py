import math
import csv

def promedio(yf, yi, xf, xi):

    pass

def pendiente(self, x, y):
    pass

with open("entrada.csv", "r") as ent:
    lector = csv.DictReader(ent)
    #crear estructura del archivo de salida con los campos necesarios, incluyendo Vx y Vy
    campos = ["VECTOR_ID", "TIEMPO", "TIEMPO_S", "VECTOR", "ANGULO_VEL_MEDIA", "VELOCIDAD_MEDIA", "Vx", "Vy", "T_prom_sec", "Vx_prom", "Vy_prom", "PENDIENTE_VX", "PENDIENTE_VY"]
    with open("salida.csv","w", newline='') as sal:
        escritor = csv.DictWriter(sal, fieldnames=campos)
        escritor.writeheader()
        for col in lector:
            #convertir casi todo a float para poder realizar la división
            tiempo = float(col["TIEMPO"])
            tiempo_s = 180
            vector = float(col["VECTOR"])
            vel_media = float(vector/(tiempo_s))
            vx = vel_media*math.cos(math.radians(float(col["ANGULO_VEL_MEDIA"])))
            vy = vel_media*math.sin(math.radians(float(col["ANGULO_VEL_MEDIA"])))
            #escribir código para obtener un valor promedio desde la columna "TIEMPO_S", dividiendo el segundo valor por el primero, el tercero por el segundo y así sucesivamente
            tiempo_s = [float(col["TIEMPO_S"])]
            for i in range(len(tiempo_s)):
                if i > 0:
                    tiempo_s.append(float(col["TIEMPO_S_"+str(i+1)]) / tiempo_s[i-1])
            t_prom_sec = sum(tiempo_s) / len(tiempo_s)
            
            escritor.writerow({"VECTOR_ID": col["VECTOR_ID"],
                               "TIEMPO": tiempo,
                               "TIEMPO_S": tiempo_s,
                               "VECTOR": float(col["VECTOR"]),
                               "ANGULO_VEL_MEDIA": col["ANGULO_VEL_MEDIA"],
                               "VELOCIDAD_MEDIA": vel_media,
                               "Vx": vx,
                               "Vy": vy})
