import csv
import matplotlib.pyplot as plt
# Función para evaluar criterio para deshechar medidas:
def crit(valores):
    promedio = sum(valores) / len(valores)
    # Calcular la varianza y la desviación típica
    varianza = sum((x - promedio) ** 2 for x in valores) / len(valores)
    desv_tip = varianza ** 0.5
    # Calcular desviacion estandar
    desv_st = ((len(valores) / (len(valores)-1)) ** 0.5) * desv_tip
    datos = [valor for valor in valores if promedio - 2*desv_st < valor < promedio + 2*desv_st]
    return datos
# Abrir archivo CSV y leerlo como lista de diccionarios:
with open('datos.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data = []
    for row in csv_reader:
        data.append(row)
# Pedir datos de sensibilidad del instrumento
sens_inst = float(input("Ingrese la sensibilidad del instrumento en cm: "))
# Extraer los valor del diccionario y guardarlos como lista. Asignar a una nueva lista los valores obtenidos, pasandolos por filtro de funcion crit::
valores = crit([float(d['distancia']) for d in data])
# Calcular el promedio, la varianza y la desviación típica
promedio = sum(valores) / len(valores)
varianza = sum((x - promedio) ** 2 for x in valores) / len(valores)
desv_tip = varianza ** 0.5
# Calcular desviacion estandar
desv_st = ((len(valores) / (len(valores)-1)) ** 0.5) * desv_tip
# calcular el error tipico
error_tip = desv_st / (len(valores) ** 0.5)
# Calcular el error instrumental usando la sensibilidad del instrumento
error_inst = sens_inst / 2
# Calcular el error absoluto usando el error instrumental
error_abs = (error_tip * 2) + error_inst
# Calcular el error relativo y el error porcentual:
error_rel = error_abs / promedio
error_porc = error_rel * 100
# Imprimir resultados parciales
print("Desviación típica:", round(desv_tip, 4))
print("Desviación estándar:", round(desv_st, 4))
print("Error típico:", round(error_tip, 4))
print("Sensibilidad instrumento:", round(sens_inst, 2))
print("Error instrumental:", round(error_inst, 2))
print("Error absoluto:", round(error_abs, 4))
print("Error relativo:", round(error_rel, 4))
print("Error porcentual:", round(error_porc, 2),"%")
print("El promedio de las mediciones es:", promedio, "±", round(error_abs, 2),"cm.")
# Calcular el tiempo promedio, pasando los cm del resultado a metros:
tiempo_prom = ((2 * (promedio * 0.01) / 9.8) ** 0.5)
# Calcular el error asociado al tiempo, pasando los cm del resultado a metros:
tiempo_error = ((2 / 9.8) ** 0.5) * ((error_abs * 0.01) / (2 * ((promedio * 0.01) ** 0.5)))
# Imprimir resultado de lo anterior:
print("El tiempo promedio de reacción es de:", round(tiempo_prom, 2), "segundos ±", round(tiempo_error, 4), "segundos")
# Contar la frecuencia de datos y almacenar como un diccionario
frec_dic = {}
for val in valores:
    if val in frec_dic:
        frec_dic[val] += 1
    else:
        frec_dic[val] = 1
# Graficar diccionario
plt.bar(frec_dic.keys(), frec_dic.values())
# Titulos del grafico
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de valores en el experimento')
# Mostrar grafico
plt.show()
