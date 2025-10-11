import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load shared library
lib = ctypes.CDLL("./1.so")

# Define function signature
lib.solvePlaneAndLine.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # A
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # B
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # C
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # P
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # Q
    ctypes.POINTER(ctypes.c_double),  # nx
    ctypes.POINTER(ctypes.c_double),  # ny
    ctypes.POINTER(ctypes.c_double),  # nz
    ctypes.POINTER(ctypes.c_double),  # d
    ctypes.POINTER(ctypes.c_double),  # ix
    ctypes.POINTER(ctypes.c_double),  # iy
    ctypes.POINTER(ctypes.c_double),  # iz
]
lib.solvePlaneAndLine.restype = None

# Given values
A = (2, 5, -3)
B = (-2, -3, 5)
C = (5, 3, -3)
P = (3, 1, 5)
Q = (-1, -3, -1)

# Prepare output variables
nx = ctypes.c_double()
ny = ctypes.c_double()
nz = ctypes.c_double()
d  = ctypes.c_double()
ix = ctypes.c_double()
iy = ctypes.c_double()
iz = ctypes.c_double()

# Call C function
lib.solvePlaneAndLine(*A, *B, *C, *P, *Q,
                      ctypes.byref(nx), ctypes.byref(ny), ctypes.byref(nz), ctypes.byref(d),
                      ctypes.byref(ix), ctypes.byref(iy), ctypes.byref(iz))

print(f"Plane equation: {nx.value:.2f}x + {ny.value:.2f}y + {nz.value:.2f}z + {d.value:.2f} = 0")
print(f"Intersection point: ({ix.value:.2f}, {iy.value:.2f}, {iz.value:.2f})")

# ---------------- Plotting ----------------

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot plane
xx, yy = np.meshgrid(range(-5, 6), range(-5, 6))
zz = (-nx.value*xx - ny.value*yy - d.value) / nz.value
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot line
t = np.linspace(-2, 2, 100)
line_x = P[0] + (Q[0]-P[0])*t
line_y = P[1] + (Q[1]-P[1])*t
line_z = P[2] + (Q[2]-P[2])*t
ax.plot(line_x, line_y, line_z, 'r-', label="Line")

# Plot intersection point
ax.scatter(ix.value, iy.value, iz.value, color='black', s=50, label="Intersection")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.savefig('1.png')
plt.show()