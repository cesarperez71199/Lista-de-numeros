# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:29:03 2023

@author: Cesar Perez
"""

import statistics 

#Lista de numeros

numeros=[7.0, 2.0, 8.3, 3.0, 5.6, 4.0]

#Imprime de la lista el num max, min, la suma y media 

print(max(numeros))

print(min(numeros))

print(sum(numeros))

mean= statistics.mean( numeros)
print(mean)

print("%5.2f" % mean)








