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
A = np.array([-2,-10,3]).reshape(-1,1)
B = np.array([1,-1,3]).reshape(-1,1)
C = np.array([3,5,3]).reshape(-1,1)



fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Flatten vectors before plotting
A, B, C = A.flatten(), B.flatten(), C.flatten()

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)

#Plotting all lines
ax.plot(x_AB[0,:],x_AB[1,:], x_AB[2,:],color='pink',label='$OA$')
ax.plot(x_BC[0,:],x_BC[1,:], x_BC[2,:],color='y',label='$OB$')

# Scatter plot
ax.scatter(*A, color='r', s=100, label='A(-2, -10, 3)')
ax.scatter(*B, color='g', s=100, label='B(1, -1, 3)')
ax.scatter(*C, color='b', s=100, label='C(3, 5, 3)')

#Annotating points
ax.text(*A, ' A', color='r', fontsize=10)
ax.text(*B, ' B', color='g', fontsize=10)
ax.text(*C, ' C', color='b', fontsize=10)

#Setting axes' labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Points A, B, C and the line passing through')
ax.legend()
ax.grid(True)

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
