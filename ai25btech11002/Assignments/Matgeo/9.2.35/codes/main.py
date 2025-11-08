import math
#import sys   
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import *

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

x1 = np.array([-2,0]).reshape(-1,1) 
x2 = np.array([2,0]).reshape(-1,1) 

#line parameters
n = np.array([0,1]).reshape(-1,1) 
c = 0

#Entering equations inmatrix form
A = np.block([[2*x1,2*x2,n],[1,1,0]]).T
b = -np.array([LA.norm(x1)**2,LA.norm(x2)**2,c]).reshape(-1,1) 
x = LA.solve(A,b)

#Centre and radius
u = x[:2]
O = -u
f = x[2][0]
r = np.sqrt(LA.norm(u)**2-f)
print(O,r)

#generating circle
x_circ= circ_gen(O,r)


#Generating Lines
k1 = -3
k2 = 3
x_A = line_norm(n,c,k1,k2)

#Plotting all lines and circles
plt.plot(x_A[0,:],x_A[1,:],label='y=0')
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')

# Shading the semicircle
xs = np.linspace(-r, r, 100)
ys = np.sqrt(r**2 - xs**2)
plt.fill_between(xs, 0, ys, color='cyan', alpha=0.5, label='Semicircle')

colors = np.arange(1,4)
#Labeling the coordinates
tri_coords = np.block([x1,x2,O])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['$P_1$','$P_2$','$O$']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-20,5), # distance from text to points (x,y)
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
'''
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
