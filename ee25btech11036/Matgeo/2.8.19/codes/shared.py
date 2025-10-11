import ctypes
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib = ctypes.CDLL("./libstp.so")
lib.scalar_triple.restype = ctypes.c_double

# Define vectors
a = (ctypes.c_double * 3)(1, 0, 0)
b = (ctypes.c_double * 3)(0, 1, 0)
c = (ctypes.c_double * 3)(1, 1, 0)

# Call the C function
result = lib.scalar_triple(a, b, c)
print("Scalar triple product =", result)

# Convert to numpy arrays for plotting
a_vec = np.array([a[0], a[1], a[2]])
b_vec = np.array([b[0], b[1], b[2]])
c_vec = np.array([c[0], c[1], c[2]])

# Plot vectors in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = np.array([0, 0, 0])

ax.quiver(*origin, *a_vec, color='r', label='a')
ax.quiver(*origin, *b_vec, color='g', label='b')
ax.quiver(*origin, *c_vec, color='b', label='c')

ax.set_xlim([0, 1.5])
ax.set_ylim([0, 1.5])
ax.set_zlim([0, 1.5])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Scalar Triple Product = {result}")
ax.legend()

plt.show()
