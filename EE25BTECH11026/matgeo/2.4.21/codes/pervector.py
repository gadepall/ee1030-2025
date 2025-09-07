import numpy as np
import matplotlib as mp
mp.use("TkAgg")
import matplotlib.pyplot as plt
import ctypes

# Load shared library
lib = ctypes.CDLL("./libcrsproduct_mag.so")   # <-- change name if your .so file is different

# Define argument and return types for the C functions
lib.find_cross_product.argtypes = [
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double)
]
lib.find_cross_product.restype = None   # because result is returned via array

lib.find_magnitude.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.find_magnitude.restype = ctypes.c_double

def cross_via_c(a, b):
    a_arr = (ctypes.c_double * 3)(*a)
    b_arr = (ctypes.c_double * 3)(*b)
    result = (ctypes.c_double * 3)()

    lib.find_cross_product(a_arr, b_arr, result)

    return np.array([result[0], result[1], result[2]], dtype=float)

a = np.array([2, 1, 2], dtype=np.int32)
b = np.array([0, 1, 1], dtype=np.int32)

# Cross product from C
x = cross_via_c(a, b)
print("Cross product :", x)

# Magnitude from C
x_ctypes = (ctypes.c_double * 3)(*x)
mag = lib.find_magnitude(x_ctypes)

# Unit vector
u = x / mag

print("Unit vector perpendicular to vectors a and b is \u00B1 [" + ", ".join(f"{val:.2f}" for val in u) + "]")
print("That is,")
print("+u =", [format(val, ".2f") for val in u])
print("-u =", [format(val, ".2f") for val in -u])

# --- Plotting ---
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.zeros(3)

# Plot a, b, and cross product directions
ax.quiver(*origin, *a, color='r', label='a', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='g', label='b', arrow_length_ratio=0.1)
ax.quiver(*origin, *u, color='c', label='(a × b)', arrow_length_ratio=0.1) 
ax.quiver(*origin, *-u, color='b', label='-(a × b)', arrow_length_ratio=0.1)

ax.set_xlim([min(a[0], b[0], u[0], -u[0], 0),
             max(a[0], b[0], u[0], -u[0], 0)])

ax.set_ylim([min(a[1], b[1], u[1], -u[1], 0),
             max(a[1], b[1], u[1], -u[1], 0)])

ax.set_zlim([min(a[2], b[2], u[2], -u[2], 0),
             max(a[2], b[2], u[2], -u[2], 0)])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.savefig("/home/user/Matrix/Matgeo_assignments/2.4.21/figs/Figure_1.png")
plt.show()

