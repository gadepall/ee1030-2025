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

# ----- Given Skew Lines -----
A1 = np.array([4, -1, 0])
d1 = np.array([1, 2, -3])
A2 = np.array([1, -1, 2])
d2 = np.array([2, 4, -5])

# ----- Closest Points (from solution) -----
lam = 3
mu = 9/5
x1 = A1 + lam*d1
x2 = A2 + mu*d2

# Flatten vectors before plotting
A1, A2, x1, x2 = A1.flatten(), A2.flatten(), x1.flatten(), x2.flatten()

# ----- Generate lines using line_gen -----
L1 = line_gen(A1, A1 + 6*d1)
L2 = line_gen(A2, A2 + 3*d2)
Normal = line_gen(x1, x2)

# ----- Plot -----
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

# Skew lines
ax.plot(L1[0,:], L1[1,:], L1[2,:], 'r', label='Line 1')
ax.plot(L2[0,:], L2[1,:], L2[2,:], 'b', label='Line 2')

# Normal line
ax.plot(Normal[0,:], Normal[1,:], Normal[2,:], 'g--', linewidth=2, label='Normal')

# Points
ax.scatter(*A1, color='r', s=50)
ax.scatter(*A2, color='b', s=50)
ax.scatter(*x1, color='orange', s=70, label='$x_1$')
ax.scatter(*x2, color='purple', s=70, label='$x_2$')

# Annotate closest points
ax.text(*x1, "  x₁", color='orange', fontsize=10)
ax.text(*x2, "  x₂", color='purple', fontsize=10)

# Axes and grid
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Skew Lines and Normal')
ax.legend()
ax.grid(True)

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
