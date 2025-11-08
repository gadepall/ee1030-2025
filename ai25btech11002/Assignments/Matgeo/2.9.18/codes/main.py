import math
#import sys   
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#if using termux
#import subprocess
#import shlex
#end if
A = np.array([-3,7,5]).reshape(-1,1)
B = np.array([-5,7,-3]).reshape(-1,1)
C = np.array([7,-5,-3]).reshape(-1,1)
O = np.array([0,0,0]).reshape(-1,1)
D = LA.det(np.block([A, B, C]))
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Flatten vectors before plotting
O, A, B, C = O.flatten(), A.flatten(), B.flatten(), C.flatten()

#Generating all lines
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OC = line_gen(O,C)

#Plotting all lines
ax.plot(x_OA[0,:],x_OA[1,:], x_OA[2,:],color='pink',label='$OA$')
ax.plot(x_OB[0,:],x_OB[1,:], x_OB[2,:],color='y',label='$OB$')
ax.plot(x_OC[0,:],x_OC[1,:], x_OC[2,:],color='purple',label='$OC$')

# Scatter plot
ax.scatter(*A, color='r', s=100, label='A(-3, 7, 5)')
ax.scatter(*B, color='g', s=100, label='B(-5, 7, -3)')
ax.scatter(*C, color='b', s=100, label='C(7, -5, -3)')

#Annotating points
ax.text(*A, ' A', color='r', fontsize=10)
ax.text(*B, ' B', color='g', fontsize=10)
ax.text(*C, ' C', color='b', fontsize=10)

#Setting axes' labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Edges of a parallelopiped')
ax.legend()
ax.grid(True)

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
