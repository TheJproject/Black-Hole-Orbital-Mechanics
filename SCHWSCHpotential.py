# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:30:17 2019

@author: Jonah
"""

import numpy as np
import matplotlib.pyplot as plt

##SCHARWSCHILD METRIC
x = np.linspace(-1.0,90.0,1000)
x1 = np.linspace(0,0,1000)
def Vs(r,M,L):
    F = (1.0-2.0*M/r)*(1.0+L**2.0/r**2.0) 
    return F
M =1

inters = np.linspace(v1[165],v1[480])
plt.figure(figsize=(7,7))
v1 =Vs(x,M,5*M)
inters = np.linspace(v1[150],v1[642],492)

minn = np.min(v1)
plt.plot(x,v1, 'k', label='$L=3.7M$')
plt.plot(x[150],v1[150], 'bo',markersize=8)
plt.plot(x[642],v1[642], 'bo',markersize=8)
plt.plot(x[150:642],inters, 'b')
#492
plt.axis([0,90,0.9,1.1])

plt.gca().axes.get_yaxis().set_visible(False)

plt.gca().axes.get_xaxis().set_visible(False)

plt.show()
plt.savefig('smallsch2', dpi=600)

