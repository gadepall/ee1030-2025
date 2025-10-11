#Code by GVV Sharma
#July 22, 2024
#released under GNU GPL
#Line 


import sys                                          #for path to external scripts
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import mpmath as mp
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

I = np.eye(2)
e1 = I[:,[0]]
e2 = I[:,[1]]

#Direction vector
m = np.array(([1, -2])).reshape(-1,1) 
n = np.array(([2, 1])).reshape(-1,1) 
c = 4

#Given points
A = np.array(([2, -2])).reshape(-1,1) 
B = np.array(([3, 7])).reshape(-1,1) 

#Section
k = (c-n.T@A)/(n.T@B-c)
print(k)
C = (k*B+A)/(k+1)

k1 = -3
k2 = 3
#Generating Lines
x_C = line_dir_pt(m,C,k1,k2)
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$distance(AB)$')
plt.plot(x_C[0,:],x_C[1,:],label='$distance(C)$')

colors = np.arange(1,4)
#Labeling the coordinates
tri_coords = np.block([A,B,C])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
    #plt.annotate(f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-10,-5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('chapters/10/7/4/1/figs/fig.pdf')
subprocess.run(shlex.split("termux-open chapters/10/7/4/1/figs/fig.pdf"))
#else
#plt.show()
