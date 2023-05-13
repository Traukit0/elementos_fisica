import numpy as np

# Definir los valores de Vy_prom y Tprom en dos arreglos separados
Vy_prom = np.array([0.7819925, 0.535047222, 0.146990833, 0.141111389, 0.035278056,
                    0.529167778, 1.117131667, 0.511528889, -0.393336111, -1.059838056,
                    -1.220013611, -1.397851944, 0.984228333, 2.710514444, 1.875605556,
                    1.728614722, 1.2700025, 1.428752778, 0.764353333])
Tprom = np.array([270, 450, 630, 810, 990, 1170, 1350, 1530, 1710, 1890, 2070, 2250,
                  2430, 2610, 2790, 2970, 3150, 3330, 3510])

# Calcular el área bajo la curva usando la regla del trapecio
areavx = np.trapz(y=Vy_prom, x=Tprom)

# Imprimir el resultado
print("El área bajo la curva para Vx es:",areavx,"metros.")


# Definir los valores de Vx_prom, y Tprom en dos arreglos separados
Vx_prom = np.array([0.064676111, 1.31116, 2.604681111, 3.233802778, 1.740373889,
                    0.593843889, 0.405695278, 0.646760556, 1.4306075, 2.173593889,
                    2.486844444, 2.794703056, 2.303208611, 3.098571111, 1.969679722,
                    0.094074167, 0.346898889, 0.305741389, 0.893705556])
Tprom = np.array([270, 450, 630, 810, 990, 1170, 1350, 1530, 1710, 1890, 2070, 2250,
                  2430, 2610, 2790, 2970, 3150, 3330, 3510])

# Calcular el área bajo la curva usando la regla del trapecio
areavy = np.trapz(y=Vx_prom, x=Tprom)

# Imprimir el resultado
print("El área bajo la curva para Vy es:",areavy,"metros.")
print("La sumatoria de ambas áreas es:",areavx+areavy,"metros")