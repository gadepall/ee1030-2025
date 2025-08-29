import sys                                          #for path to external scripts
sys.path.insert(0, 'D:\codes\CoordGeo')        #path to my scriptsimport numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

# Given points
A = np.array([2, -2]).reshape(-1, 1)
B = np.array([-7, 4]).reshape(-1, 1)

# Calculate the points of trisection
# P divides AB in the ratio 1:2
P = (2*A + 1*B) / 3
# Q divides AB in the ratio 2:1
Q = (1*A + 2*B) / 3

# Generate the line segment AB
x_AB = np.array([A[0,0], B[0,0]])
y_AB = np.array([A[1,0], B[1,0]])

# Plotting the line
plt.plot(x_AB, y_AB, label='AB')

# Plotting the points
tri_coords = np.block([[A, B, P, Q]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])

# Labeling the coordinates
vert_labels = ['A', 'B', 'P', 'Q']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

# Set plot aesthetics
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')

#if using termux
plt.savefig('E:\python1')
#else
#plt.show()
