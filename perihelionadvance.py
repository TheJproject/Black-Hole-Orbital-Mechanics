# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:27:50 2019

@author: Jonah
"""

import numpy as np
import matplotlib.pyplot as plt

cos = np.cos
sin=np.sin
pi = np.pi

a = 10
e = 0.8
m = 5
L = m*a*(1.0-e**2)


theta = np.linspace(0,42*pi, 21*360)

r =(1/L)+(1/L**2)*(1+(e**2)/3)+(e/L)*cos((1-1/L)*theta)+((e**2)/(3*L**2))*(cos(2*theta))

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_yticklabels([])
ax.plot(theta,r**-1)
ax.fill_between(np.linspace(0.0, 2*pi,200), 2.0*np.ones(200),facecolor='black') 
#ax.set_rmax(15)

plt.show()
plt.savefig('periadv_2', dpi=600)









