# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 10:48:33 2019

@author: Wojciech
"""

import numpy as np
import pandas as pd
class which:
    def min_w(lista):
        x = pd.DataFrame(lista)
        x = x.ix[:,0]
        lw = len(np.where(x == min(x))[0])
        
        list_min = []
        for i in range(0, lw):
            value = (np.where(x == min(x))[0][i])
            list_min.append(value)
        
        return(list_min)
        
    def max_w(lista):
        x = pd.DataFrame(lista)
        x = x.ix[:,0]
        lw = len(np.where(x == max(x))[0])
        
        list_max = []
        for i in range(0, lw):
            value = (np.where(x == max(x))[0][i])
            list_max.append(value)
        
        return(list_max)
    
    def equal(lista, equals):
        x = pd.DataFrame(lista)
        x = x.ix[:,0]
        lw = len(np.where(x == equals)[0])
        
        list_equals =[]
        for i in range(0, lw):
            value = np.where(x == equals)[0][i]
            list_equals.append(value)
            
        return(list_equals)
        
    def HigherThan(lista, Higher):
        x = pd.DataFrame(lista)
        x = x.ix[:, 0]
        lw = len(np.where(x > Higher)[0])
        
        list_higher = []
        for i in range(0, lw):
            value = np.where(x > Higher)[0][i]
            list_higher.append(value)
            
        return(list_higher)
    
    def LessThan(lista, Less):
        x = pd.DataFrame(lista)
        x = x.ix[:, 0]
        lw = len(np.where(x < Less)[0])
        
        list_less = []
        for i in range(0, lw):
            value = np.where(x < Less)[0][i]
            list_less.append(value)
            
        return(list_less)
        
    def LessThanAndEqual(lista, LessAndEqual):
        x = pd.DataFrame(lista)
        x = x.ix[:, 0]
        lw = len(np.where(x <= LessAndEqual)[0])
        
        list_LessAndEqual = []
        for i in range(0, lw):
            value = np.where(x <= LessAndEqual)[0][i]
            list_LessAndEqual.append(value)
            
        return(list_LessAndEqual)
    
    def HigherThanAndEqual(lista, HigherandEqual):
        x = pd.DataFrame(lista)
        x = x.ix[:, 0]
        lw = len(np.where(x >= HigherandEqual)[0])
        
        list_HigherandEqual = []
        for i in range(0, lw):
            value = np.where(x >= HigherandEqual)[0][i]
            list_HigherandEqual.append(value)
            
        return(list_HigherandEqual)


import random

x = []
for i in range(0, 100):
    y = random.randint(0, 10)
    x.append(y)

which.equal(x, 5)
which.HigherThanAndEqual(x, 9)
which.max_w(x)
which.min_w(x)
which.LessThan(x, 2)
x

which.equal(x, 5) ## MOJA FUNKCJA
np.where(pd.DataFrame(x) == 5)
