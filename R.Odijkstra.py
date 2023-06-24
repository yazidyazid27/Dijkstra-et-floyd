# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:27:07 2022

@author: yazid
"""

# 

import math
import numpy as np
from numpy import inf
def dijkstra(M, depart):
    #la distance du sommet de depart vers tous les autres sommets
    distances = [float("inf") for _ in range(len(M))]
    #les sommets qui sont deja visités
    visiter = [False for _ in range(len(M))]
    #initialiser la distance du sommet de depart à lui-meme qui vaut 0
    distances[depart] = 0
    #Tant qu'il y a toujours des sommets à visiter alors on execute la boucle
    while True:
        # On cherche le sommet de distance minimale du sommet de depart
        distance_min = float("inf")
        indice_min = -1
        for i in range(len(M)):
            if distances[i] < distance_min and not visiter[i]:
                distance_min = distances[i]
                indice_min = i

        if indice_min == -1:
            # tous les sommets sont visités alors on a fini
            return distances
        # pour le reste des sommets non encore visités 
        for i in range(len(M[indice_min])):
            if M[indice_min][i] != 0 and distances[i] > distances[indice_min] + M[indice_min][i]:
                distances[i] = distances[indice_min] + M[indice_min][i]
        visiter[indice_min] = True
        
        
Mat = np.array([[ 0, 8, 2, inf, inf, inf, inf]
                 ,[inf, 0, inf, inf, 3, inf, 10] 
                 ,[inf, inf, 0, 3, inf, inf, inf] 
                 ,[inf, 2, 4, 0, inf, inf, inf]
                 ,[inf, inf, 5, inf, 0, 4, inf]
                 ,[inf, 5, inf, inf, 2, 0, 2]
                 ,[inf, inf, inf, inf, inf, inf, 0]])

# print(Mat)   
# for i in range(7):
#     print(dijkstra(Mat, i), "pour I=",i)
print(dijkstra(Mat, 0)  )


