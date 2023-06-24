# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 00:00:13 2022

@author: yazid
"""

import numpy as np
from numpy import inf

def FloydAlg(M,nombre_sommet):
    n=nombre_sommet

    pred = np.zeros(M.shape) 
    for i in range(n): 
        for j in range(n):
            pred[i,j] = i 
            if (i != j and M[i,j] == 0): 
                pred[i,j] = -10000 
                M[i,j] = 10000
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (M[i,j]>M[i,k]+M[k,j]):
                    M[i,j]=M[i,k]+M[k,j]
                    pred[i,j] = pred[k,j]
    return(M)
#les chemin
def Chemins(p, i, j): 
    i,j = int(i), int(j) 
    if(i==j):
        print (i,) 
    elif(p[i,j] == -10000):
        print (i,'-',j) 
    else: 
        Chemins(p, i, p[i,j])
        print(j,) 
M1 = np.array([[ 0, 8, 2, inf, inf, inf, inf]
                 ,[inf, 0, inf, inf, 3, inf, 10] 
                 ,[inf, inf, 0, 3, inf, inf, inf] 
                 ,[inf, 2, 4, 0, inf, inf, inf]
                 ,[inf, inf, 5, inf, 0, 4, inf]
                 ,[inf, 5, inf, inf, 2, 0, 2]
                 ,[inf, inf, inf, inf, inf, inf, 0]])

nombre_sommet=7
M2 = np.array([[0 ,8 ,inf ,inf ,2 ]
              ,[8 ,0 ,5 ,1 ,4 ]
              ,[inf ,5 ,0 ,2 ,inf ]
              ,[inf ,1 ,2 ,0 ,2 ]
              ,[2 ,4 ,inf ,2 ,0 ]])
nombre_sommet=5
print(M2)
print(FloydAlg(M2,nombre_sommet))

print(Chemins(FloydAlg(M2,nombre_sommet),4,1))
