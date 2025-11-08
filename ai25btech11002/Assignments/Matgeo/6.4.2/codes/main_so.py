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
import ctypes
# Load compiled shared library (Linux example)
lib = ctypes.CDLL("./closest_point.so")

# Define argtypes and restype
lib.calc_lambda_mu.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),  # A1
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),  # d1
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),  # A2
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),  # d2
    ctypes.POINTER(ctypes.c_double),  # lambda
    ctypes.POINTER(ctypes.c_double)   # mu
]
lib.calc_lambda_mu.restype = None

# Input arrays
A1 = np.array([4.0, -1.0, 0.0], dtype=np.double)
d1 = np.array([1.0, 2.0, -3.0], dtype=np.double)
A2 = np.array([1.0, -1.0, 2.0], dtype=np.double)
d2 = np.array([2.0, 4.0, -5.0], dtype=np.double)

lam = ctypes.c_double()
mu = ctypes.c_double()

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
