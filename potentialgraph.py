# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 19:45:31 2019

@author: Jonah
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)
    

x = np.linspace(-1.0,15.0,1000)
x1 = np.linspace(0,0,1000)


def V(r,J):
    F = -(r**-1.0)+0.5*(J**2)*(r**-2.0)
    return F

v1 =V(x,1)
minn  = np.min(v1)
x2 = np.linspace(4.0,100,1000)
x3 = np.linspace(0,100,1000)
v199=np.linspace(-0.25,-0.25,177)
#v180=np.linspace(0.3,0.3,810)
vpara=np.linspace(0.0,0.0,807)
plt.plot(x,v1, 'k',  label='$y_1$')
#plt.plot(x[99:276],v199, 'b',  label='$y_1$')
#plt.plot( x[99],-0.25, 'bo',markersize=8)

#plt.plot( x[276],-0.25, 'bo',markersize=8)
#plt.plot(x[93:900],vpara, 'b',  label='$y_1$')
#plt.plot( x[93],0.0, 'bo',markersize=8)
#
plt.plot(x,x1, color='grey',linestyle='--')
#plt.plot( 1.01,minn, 'bo',markersize=8)
#plt.plot(x,x2, color='lightblue',linestyle='--')
plt.arrow(20.0,0.3,-15.0,0.0,width=0.0018)
plt.text(5.7,0.37,'$E$',size=20)

"""


plt.text(5.88, 0.5, r'\textac{Hyperbolic}', fontsize= 18)
plt.text(5.88, 0.02, r'\textac{Parabolic}', fontsize= 18, color='red')
plt.text(5.88, -0.33, r'\textac{Circular}', fontsize= 18, color='blue')
plt.text(7.5, -0.2, r'\textac{Elliptic}', fontsize= 18)
"""
#plt.plot(x,x3, 'r--')
        

plt.xlabel('$r$')
plt.ylabel('$V_{eff}(r)$')
#plt.legend(loc='upper right')
"""
plt.fill_between(x,0,x3, facecolor='grey', alpha=0.3)
plt.fill_between(x,0,minn, facecolor='red', alpha=0.3)
"""
plt.axis([0,12,-0.8,0.7])
#plt.gca().axes.get_yaxis().set_visible(False)

#plt.gca().axes.get_xaxis().set_visible(False)

plt.show()
plt.savefig('potential1.png', dpi=600)

