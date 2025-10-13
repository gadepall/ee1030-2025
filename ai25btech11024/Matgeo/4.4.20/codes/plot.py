import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *

#Given Points
A = np.array([6,1.2]).reshape(-1,1)
B = np.array([-3,-2.4]).reshape(-1,1)

#Generating Lines
x_A = line_gen(A,B)

#Plotting all lines
plt.plot(x_A[0,:],x_A[1,:])

#Labeling the coordinates
tri_coords = np.block([A,B])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c='red')

plt.text(A[0],A[1],"A")
plt.text(B[0],B[1],"B")

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/img.png')
plt.show()
