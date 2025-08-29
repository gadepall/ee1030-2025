#Secion Formula


import sys                                                 
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

#Given points
A = np.array(([1,3])).reshape(-1,1)
B = np.array(([4,6])).reshape(-1,1)

#Ratio
n=2/1

#Point
P= (A+n*B)/(1+n) # calculating the coordinate points of R which divides the join between the two points
#print(R)

#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

#Labeling the coordinates
tri_coords = np.block([[A,B,P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,-10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
# use set_position
ax = plt.gca()
#ax.spines['top'].set_color('none')
#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
#plt.xlabel('$x$')
#plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
