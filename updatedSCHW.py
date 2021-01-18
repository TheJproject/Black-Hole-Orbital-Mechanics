# -*- coding: utf-8 -*-
"""
Created on Thu May 02 21:35:48 2019

@author: Jonah
"""

import numpy as np
import matplotlib.pyplot as plt



##SCHARWSCHILD METRIC
def Vs(r,M,L):
    F = (1.0-2.0*M/r)*(1.0+L**2.0/r**2.0) 
    return F

#Kepler Potential
def V(r,M,L):
    F = -(r**-1.0)+((L**2)*0.5*(r**-2.0))+0.97
    return F
    
x0=np.linspace(0.0,0.0,1000)   
fig, ax = plt.subplots(figsize=(7,7))
fig.set_figwidth(7)
fig.set_figheight(7)
x = np.linspace(-1.0,50.0,1000)
K = V(x,1,4)    

F=np.zeros([4,1000])
L=np.array([4.0,3.7,3.0,np.sqrt(12)]) 
for i in range(4):
    F[i]=Vs(x,1,L[i])
    
l1, = ax.plot(x, F[0],color='navy', label='$L=4M$')
l2, = ax.plot(x, F[1],color='darkblue', label='$L=3.7M$')
l4, = ax.plot(x, F[3],color='mediumblue', label='$L=2\sqrt{3}M$')
l3, = ax.plot(x, F[2],color='b', label='$L=3M$')
l5, = ax.plot(x, K,'r',linestyle='--', label='Keplerian approx.')

ax.axvspan(0, 2, alpha=0.5, color='red')
#ax.fill_between(x,x0,F[3] ,facecolor='grey', alpha=0.3)
ax.set_xlabel("$r$")
ax.set_ylabel("$V(r)$")
ax.set_xlim([0, 20])
ax.set_ylim([0.6, 1.1])
plt.legend(handles=[l1,l2,l4,l3,l5],loc='lower right')

plt.show(fig)
plt.savefig('SCHwarplot.png', dpi=600)
