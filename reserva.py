"""
Reserva de un asiento en sala de cine
Tarea Semana 12 - Unidad 3. Arreglos N-Dimensionales
Tema 3.2.2. Iteracion sobre arreglos multidimensionales utilizando bucles anidados

Autor: Malla Alban Dennys Bladimir
Objetivo: Gestionar la reserva de asientos de una sala de cine de 3 filas
por 4 columnas, utilizando una matriz (lista de listas) y bucles anidados
para mostrar el estado completo de la sala.
"""

# Numero de filas y columnas de la sala
NUM_FILAS = 3
NUM_COLUMNAS = 4

# Crear la matriz "asientos" de 3 filas por 4 columnas, inicializada en 0
# 0 = asiento libre, 1 = asiento reservado
asientos = []
for i in range(NUM_FILAS):
    fila_actual = []
    for j in range(NUM_COLUMNAS):
        fila_actual.append(0)
    asientos.append(fila_actual)

# Solicitar al usuario la fila y la columna del asiento a reservar
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Validar que la fila y la columna esten dentro del rango permitido
if 0 <= fila < NUM_FILAS and 0 <= columna < NUM_COLUMNAS:
    # Avisar si el asiento ya estaba reservado (mejora opcional)
    if asientos[fila][columna] == 1:
        print("Aviso: ese asiento ya estaba reservado.")
    # Marcar el asiento como reservado
    asientos[fila][columna] = 1
else:
    print("Fila o columna fuera de rango. No se realizo ninguna reserva.")

# Mostrar el estado completo de la sala recorriendo la matriz
# con dos bucles anidados (uno para filas, otro para columnas)
print("Estado de la sala:")
for i in range(NUM_FILAS):
    for j in range(NUM_COLUMNAS):
        print(asientos[i][j], end=" ")
    print()  # Salto de linea al terminar cada fila
