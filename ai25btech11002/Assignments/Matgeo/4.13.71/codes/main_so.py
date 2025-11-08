import math
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import *
import ctypes
#if using termux
import subprocess
import shlex
#end if
a, b = 2, 3

# Load the shared library
lib = ctypes.CDLL('./libcoplanar.so')
lib.compute_c.argtypes = [ctypes.c_double, ctypes.c_double]
lib.compute_c.restype = ctypes.c_double

# Compute c using the C function
c = lib.compute_c(a, b)

A = np.array([a, 1, 1]).reshape(-1, 1)
B = np.array([1, b, 1]).reshape(-1, 1)
C = np.array([1, 1, c]).reshape(-1, 1)
O = np.array([0, 0, 0]).reshape(-1, 1)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Flatten vectors before plotting
O, A, B, C = O.flatten(), A.flatten(), B.flatten(), C.flatten()

#Generating all lines
x_OA = line_gen(O, A)
x_OB = line_gen(O, B)
x_OC = line_gen(O, C)

#Plotting all lines
ax.plot(x_OA[0, :], x_OA[1, :], x_OA[2, :], color='pink', label='$OA$')
ax.plot(x_OB[0, :], x_OB[1, :], x_OB[2, :], color='y', label='$OB$')
ax.plot(x_OC[0, :], x_OC[1, :], x_OC[2, :], color='purple', label='$OC$')

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = (2 * X + Y) / 5
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan')

# Scatter plot
ax.scatter(*A, color='r', s=100, label='A')
ax.scatter(*B, color='g', s=100, label='B')
ax.scatter(*C, color='b', s=100, label='C')

# Annotating points
ax.text(*A, ' A', color='r', fontsize=10)
ax.text(*B, ' B', color='g', fontsize=10)
ax.text(*C, ' C', color='b', fontsize=10)

# Setting axes' labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Co-planar vectors')
ax.legend()
ax.grid(True)

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
