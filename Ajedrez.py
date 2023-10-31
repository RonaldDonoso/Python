# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:16:07 2023

@author: FORMACION
"""

# Coordenadas de las torres
torre1 = (3, 2)
torre2 = (3, 5)

# Verificar si las torres están en la misma fila o columna
if torre1[0] == torre2[0] or torre1[1] == torre2[1]:
    print("¡Alerta! Las torres se amenazan ¡Alerta!")
else:
    print("No hay amenaza torres amenazadas")


# Coordenadas de las alfil

alfil1 = (1, 1)
alfil2 = (5, 7)

# Verificar si los alfiles se amenazan en diagonal
fila = abs(alfil1[0] - alfil2[0])
columna = abs(alfil1[1] - alfil2[1])

if fila == columna:
    print("¡Alerta! Los alfiles se amenazan ¡Alerta!")
else:
    print("No hay amenaza entre los alfiles")
    
    

# Coordenadas de las peon

peon1 = (4, 3)
peon2 = (5, 3)

# Verificar si los peones se amenazan en diagonal
fila = abs(peon1[0] - peon2[0])
columna = abs(peon1[1] - peon2[1])

if fila == 1 and columna == 1:
    print("¡Alerta! Los peones se amenazan ¡Alerta!")
else:
    print("No hay amenaza entre los peones")
