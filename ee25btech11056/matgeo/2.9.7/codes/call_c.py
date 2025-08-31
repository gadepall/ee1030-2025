import sys
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load shared object
lib = ctypes.CDLL("./points.so")
lib.box_product.restype = ctypes.c_double

# Call the C function
box = lib.box_product()
print("Box product (from C) =", box)

# Define vectors
a = np.array([2,1,3])
b = np.array([-1,2,1])
c = np.array([3,1,2])

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.array([0,0,0])

# Plot vectors with arrowheads
ax.quiver(*origin, *a, color='r', arrow_length_ratio=0.1, label="a = (2,1,3)")
ax.quiver(*origin, *b, color='g', arrow_length_ratio=0.1, label="b = (-1,2,1)")
ax.quiver(*origin, *c, color='b', arrow_length_ratio=0.1, label="c = (3,1,2)")

# Set limits
ax.set_xlim([-2,4])
ax.set_ylim([-2,4])
ax.set_zlim([0,4])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Vectors a, b, c (Box product = {box:.2f})")
ax.legend()

plt.savefig("vectors.png")
plt.show()

