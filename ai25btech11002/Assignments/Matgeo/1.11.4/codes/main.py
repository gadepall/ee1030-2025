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
A = np.array([-2,-1,2]).reshape(-1,1)
B = np.array([-6,-3,6]).reshape(-1,1)
O = np.array([0,0,0]).reshape(-1,1)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Flatten vectors before plotting
A, B, O = A.flatten(), B.flatten(), O.flatten()

#Generating all lines
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)

#Plotting all lines
ax.plot(x_OA[0,:],x_OA[1,:], x_OA[2,:],color='pink',label='$OA$')
ax.plot(x_OB[0,:],x_OB[1,:], x_OB[2,:],color='y',label='$OB$')

# Scatter plot
ax.scatter(*A, color='r', s=100, label='A(-2, -1, 2)')
ax.scatter(*B, color='g', s=100, label='B(6, -3, 6)')
ax.scatter(*O, color='b', s=100, label='O(0, 0, 0)')

#Annotating points
ax.text(*A, ' A', color='r', fontsize=10)
ax.text(*B, ' B', color='g', fontsize=10)
ax.text(*O, ' O', color='b', fontsize=10)

#Setting axes' labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('A vector B of magnitude 9 in direction of A')
ax.legend()
ax.grid(True)

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
