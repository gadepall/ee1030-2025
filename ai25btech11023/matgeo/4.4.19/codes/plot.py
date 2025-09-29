#Code by Pratik R

#Line 


import sys                                          
import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

I = np.eye(2)
e1 = I[:,[0]]
e2 = I[:,[1]]

#Direction vector
m = np.array(([2, -3])).reshape(-1,1) 

#Give point
P = np.array(([0, 2])).reshape(-1,1) 

k1 = -2
k2 = 1
#Generating Lines
x_PQ = line_dir_pt(m,P,k1,k2)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$3x+2y=4$')

colors = np.arange(1,2)
#Labeling the coordinates
tri_coords = np.block([[P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['P']
for i, txt in enumerate(vert_labels):
#    plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,20), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../figs/fig.pdf')
