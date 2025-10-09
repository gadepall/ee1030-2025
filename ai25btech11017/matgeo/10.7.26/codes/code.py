#Program to plot the focal chord tangent to a circle
#Code by GVV Sharma (Modified for Qn)
#Released under GNU GPL
#October 2025

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys

#path to local scripts
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')

#local imports
from line.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

#Parabola y^2 = 16x
y = np.linspace(-8,8,400)
x_parab = y**2/16

#Circle (x-6)^2 + y^2 = 2
theta = np.linspace(0,2*np.pi,200)
x_circ = 6 + np.sqrt(2)*np.cos(theta)
y_circ = np.sqrt(2)*np.sin(theta)

#Focus
F = np.array([[4],[0]])

#Slopes of focal chord tangent to circle (calculated analytically)
slopes = [-1,1]
x_vals = np.linspace(-2,10,200)

#Generate tangent lines and tangent points
for m in slopes:
    y_vals = m*(x_vals-4)
    plt.plot(x_vals,y_vals,'--',label=f'Chord slope {m}')
    # Tangency points (x=5,y=m)
    x_t, y_t = 5, m
    plt.scatter(x_t,y_t,c='g')
    plt.annotate(f'({x_t},{y_t})',(x_t,y_t),xytext=(10,10),
                 textcoords="offset points",ha='center',color='g')

#Plot parabola
plt.plot(x_parab,y,label='Parabola $y^2=16x$',color='r')

#Plot circle
plt.plot(x_circ,y_circ,label='Circle $(x-6)^2+y^2=2$',color='b')

#Mark focus
plt.scatter(F[0],F[1],c='k')
plt.annotate("F(4,0)",(F[0],F[1]),xytext=(10,-10),
             textcoords="offset points")

#Axes formatting
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid()
plt.axis('equal')

#if using termux
plt.savefig('chapters/11/11/2/2/figs/fig.pdf')
subprocess.run(shlex.split("termux-open chapters/11/11/2/2/figs/fig.pdf"))
#else
#plt.show()
