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
O = np.array([0,0,0]).reshape(-1,1)
A = np.array([1,-2,1]).reshape(-1,1)
B = np.array([-2,4,5]).reshape(-1,1)
C = np.array([1,-6,-7]).reshape(-1,1)

with open("data.dat", "r") as fptr: 
     line = fptr.read()
     data_list = [float(x) for x in line.split()]
     
R = np.array(data_list).reshape(3, 1)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Flatten vectors before plotting
O, A, B, C, R = O.flatten(), A.flatten(), B.flatten(), C.flatten(), R.flatten()

#Generating all lines
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OC = line_gen(O,C)
x_OR = line_gen(O,R)

#Plotting all lines
ax.plot(x_OA[0,:],x_OA[1,:], x_OA[2,:],color='r',label='$OA$')
ax.plot(x_OB[0,:],x_OB[1,:], x_OB[2,:],color='g',label='$OB$')
ax.plot(x_OC[0,:],x_OC[1,:], x_OC[2,:],color='b',label='$OC$')
ax.plot(x_OR[0,:],x_OR[1,:], x_OR[2,:],color='y',label='$OR$')

# Scatter plot
ax.scatter(*A, color='r', s=100, label='A(1, -2, 1)')
ax.scatter(*B, color='g', s=100, label='B(-2, 4, 5)')
ax.scatter(*C, color='b', s=100, label='C(1, -6, -7)')
ax.scatter(*R, color='y', s=100, label='R(0, -4, -1)')

#Annotating points
ax.text(*A, ' A', color='r', fontsize=10)
ax.text(*B, ' B', color='g', fontsize=10)
ax.text(*C, ' C', color='b', fontsize=10)
ax.text(*R, ' R', color='y', fontsize=10)

#Setting axes' labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Vectors A, B, C and their resultant R')
ax.legend()
ax.grid(True)

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
