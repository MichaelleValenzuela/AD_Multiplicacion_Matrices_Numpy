#Multiplicacion de matrices con numpy

import numpy as np
import os

print ("MATRIZ 1")
fM1 = int(input("Ingrese el numero de filas: "))
cM1 = int(input("Ingrese el numero de columnas: "))
print()
print ("MATRIZ 2")
fM2 = int(input("Ingrese el numero de filas: "))
cM2 = int(input("Ingrese el numero de columnas: "))

while (cM1 != fM2):
    print("\nError en los valores ingresados\n")
    cM1 = int(input("Numero de columnas de la Matriz 1: "))
    fM2 = int(input("Numero de filas de la Matriz 2: "))
    if (cM1 == fM2):
        break

M1 = np.zeros((fM1, cM1))
M2 = np.zeros((fM2, cM2))
R = np.zeros((fM1, cM2))

print("\nIngrese los valores de la Matriz 1\n")
for i in range(fM1):
    for j in range(cM1):
        M1[i][j] = int(input("Fila {} , Columna {}: ".format(i + 1, j + 1)))

print("\nIngrese los valores de la Matriz 2\n")
for i in range(fM2):
    for j in range(cM2):
        M2[i][j] = int(input("Fila {} , Columna {}: ".format(i + 1, j + 1)))
print()
print("Resultado matriz C: \n", np.dot(M1, M2))