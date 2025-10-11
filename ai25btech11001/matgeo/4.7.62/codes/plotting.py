import math
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from line.funcs import *

A = np.array([5,2,-4]).reshape(-1,1)

a,b,c,d=2,3,-1,20

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10,10,50)
y = np.linspace(-10,10,50)
X,Y=np.meshgrid(x,y)

Z = (d - a*X - b*Y)/c

ax.scatter(A[0],A[1],A[2],color = 'blue')
ax.plot_surface(X,Y,Z)


#ax.text(A[0],A[1],"A(-2,3)")
"""ax.xlabel('$x$')
ax.ylabel('$y$')
ax.zlabel('$z$')"""
ax.grid() # minor
ax.axis('equal')

plt.savefig('../figs/img.png')
