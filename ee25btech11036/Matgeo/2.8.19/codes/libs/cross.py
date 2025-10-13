#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Cross Product


import sys                                          #for path to external scripts
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
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

#Given points
A = np.array(([0,-1])).reshape(-1,1)
B = np.array(([2,1])).reshape(-1,1)
C = np.array(([0,3])).reshape(-1,1)

P=0.5*(A+B)
Q=0.5*(B+C)
R=0.5*(A+C)
ar1=0.5*(LA.norm(np.cross((P-Q).T,(Q-R).T)))
ar2=0.5*(LA.norm(np.cross((A-B).T,(A-C).T)))
print(ar1/ar2)

#Generating Lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$distance(AB)$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$distance(BC)$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$distance(CA)$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$distance(CA)$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$distance(CA)$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$distance(CA)$')

colors = np.arange(1,7)
#Labeling the coordinates
tri_coords = np.block([[A,B,C,P,Q,R]])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['A','B','C','P','Q','R']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
#    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,0), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
'''
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('chapters/10/7/3/3/figs/fig.pdf')
subprocess.run(shlex.split("termux-open chapters/10/7/3/3/figs/fig.pdf"))
#else
#plt.show()
