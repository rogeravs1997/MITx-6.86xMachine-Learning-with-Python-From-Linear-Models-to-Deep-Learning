# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:27:26 2021

@author: roger
"""

import numpy as np

u=[6,0,3,6]
u=np.array(u)
u.shape=(-1,1)

v=[4,2,1]
v=np.array(v)
v.shape=(-1,1)

z=u.dot(v.T)
Y=np.array([[5,"",7],["",2,""],[4,"",""],["",3,6]])


error=0

for i in range(len(Y)):
    for j in range(len(Y[i])):
        try:
            error+=(int(Y[i][j])-(z[i][j]))**2
        except:
            pass
    
print(error/2)