import ctypes
import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0, '/home/soma-harsha/Desktop/matgeo/codes/CoordGeo')
# Load shared library
lib = ctypes.CDLL("./libvectors.so")

# Set return types
lib.get_v1.restype = ctypes.POINTER(ctypes.c_double)
lib.get_v2.restype = ctypes.POINTER(ctypes.c_double)

from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Get vectors
v1 = np.array([lib.get_v1()[i] for i in range(3)])
v2 = np.array([lib.get_v2()[i] for i in range(3)])

print("v1 =", v1)
print("v2 =", v2)

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

origin = np.array([0,0,0])

# Plot vectors
ax.quiver(*origin, *v1, color='r', label="v1")
ax.quiver(*origin, *v2, color='b', label="v2")

# Line of collinearity
t = np.linspace(-2, 2, 100)
line = np.outer(t, v1)
ax.plot(line[:,0], line[:,1], line[:,2], 'g--', label="Line of Collinearity")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Collinear Vectors")
ax.legend()
plt.savefig('../figs/fig1.png')
plt.show()


