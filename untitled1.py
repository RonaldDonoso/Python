# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1owol6NnR57c4jynivZXkW_c3Yq83y01Z
"""

f1 = int(input("Ingrese la fila de la primera casa: "))
c1 = int(input("Ingrese la columna de la primera casa: "))
f2 = int(input("Ingrese la fila de la segunda casa: "))
c2 = int(input("Ingrese la columna de la segunda casa: "))

distancia = ((f2 - f1) ** 2 + (c2 - c1) ** 2) ** 0.5

print("La distancia entre las dos casas es:", distancia)