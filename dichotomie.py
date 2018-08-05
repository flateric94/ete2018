#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:43:26 2018

@author: eric
"""

def f(x):
    return(6*x+1)
    
def dicho(a,b,n):
    for i in range(n):
        m=(a+b)/2
        if f(a)*f(b)>0:
            return('pas de solution')
        elif f(a)*f(m)<=0:
            b=m
        else:
            a=m
    return(a,b)
    
print(dicho(-1,2,78))
print(dicho(3,4,1))
print(dicho(-243,23,87))
print(dicho(6,545,56))