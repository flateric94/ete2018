#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 11:09:01 2018

@author: eric
"""
def exo(n): #Papa:faire une liste de nombre
    liste=[]
    for i in range(n):
        liste.append(i+1) #i+1 si on veut de 1 à 30, sinon 0 à 29
    return(liste)
    
#print(exo(30))

def exo2(n): #Papa:ne mettre que les impairs, et pas non plus 5 ni 13 puis supprimer un indice
    liste2=[]
    for i in range(n):
        if i%2==1:
            if i not in [5,13]:
                liste2.append(i)
    del liste2[-6]
    return(liste2)
 
#print(exo2(30))

def exo3(n): #Papa: faire une liste d'impairs en s'arretant à 35
    liste3=[0]
    i=0
    while i<=35:
        if i%2==1:
            liste3.append(i)
        i=i+1
    return(liste3)
    
print(exo3(23))