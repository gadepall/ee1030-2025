import ctypes
import numpy as np
import os

# Load the shared library
libname = "libgeometry.so" if os.name != "nt" else "geometry.dll"
geometry = ctypes.CDLL(libname)

# Prepare cross product function signature
geometry.crossProduct.argtypes = [ctypes.POINTER(ctypes.c_float),
ctypes.POINTER(ctypes.c_float),
ctypes.POINTER(ctypes.c_float)]
geometry.crossProduct.restype = None

# --- Step 1: Define planes ---
n1 = np.array([1.0, 1.0, 1.0], dtype=np.float32)
n2 = np.array([2.0, 3.0, -1.0], dtype=np.float32)

# Step 2: Get direction vector = cross(n1, n2)
dir_vector = np.zeros(3, dtype=np.float32)
geometry.crossProduct(n1.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
n2.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
dir_vector.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))

# Step 3: Solve for a point on the intersection line (let x = 0)
# Equation A: y + z = 1
# Equation B: 3y - z = -4

# Solve 2x2 system:
# From:
#   y + z = 1
#   3y - z = -4
# Add: (4y = -3) => y = -0.75
# Then: z = 1 - y = 1.75

y = -0.75
z = 1.75
point = np.array([0.0, y, z], dtype=np.float32)

# Step 4: Use x-axis vector
x_axis = np.array([1.0, 0.0, 0.0], dtype=np.float32)

# Step 5: Cross product of dir and x-axis = normal vector of new plane
normal = np.zeros(3, dtype=np.float32)
geometry.crossProduct(dir_vector.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
x_axis.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
normal.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))

# Step 6: Compute 'd' in plane equation
d = -(normal @ point)  # dot product

# --- Final Result ---
print("Equation of the required plane:")
print(f"{normal[0]:.2f}x + {normal[1]:.2f}y + {normal[2]:.2f}z + {d:.2f} = 0")
