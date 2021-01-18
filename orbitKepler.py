# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:03:38 2019

@author: Jonah
"""

import numpy as np
import matplotlib.pyplot as plt
cos = np.cos
sin=np.sin
pi = np.pi
theta = np.linspace(0,2*pi, 360)

e =np.array([0.0 , 0.55, 1.0, 2.2])
r = np.zeros((4,360))
for  i in range(0,4):
    p=10
    r[i]=p/(1.0+e[i]*cos(theta))


fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_yticklabels([])
ax.set_ylim(30, 0)

#ax.plot(theta,r[1])
#ax.plot(theta,r[2])
#   ax.plot(theta,r[3])
ax.plot(theta,r[0])

plt.show()