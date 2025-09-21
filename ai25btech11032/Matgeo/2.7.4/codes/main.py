import ctypes
import numpy as np
import math
import matplotlib.pyplot as plt

# --- Load compiled C library ---
lib = ctypes.CDLL("./libgram.so")

# Define ctypes array types
DoubleArray3 = ctypes.c_double * 3
DoubleMatrix3 = (DoubleArray3) * 3

# Function signatures
lib.dot_product.argtypes = [DoubleArray3, DoubleArray3]
lib.dot_product.restype = ctypes.c_double

lib.gram_matrix.argtypes = [DoubleArray3, DoubleArray3, DoubleArray3, DoubleMatrix3]
lib.det3.argtypes = [DoubleMatrix3]
lib.det3.restype = ctypes.c_double

# --- Define vectors ---
a = np.array([2.0, 1.0, 3.0])
b = np.array([-1.0, 2.0, 1.0])
c = np.array([3.0, 1.0, 2.0])

# Convert to C arrays
A = DoubleArray3(*a)
B = DoubleArray3(*b)
C = DoubleArray3(*c)

# --- Step 1: Build Gram matrix ---
G = DoubleMatrix3()
lib.gram_matrix(A, B, C, G)

# --- Step 2: Compute det(G) ---
detG = lib.det3(G)
print("det(G) =", detG)

# --- Step 3: Magnitude of scalar triple product ---
magnitude = math.sqrt(detG)
print("|a · (b × c)| =", magnitude)

# --- Step 4: Compute sign using det(A) ---
A_mat = np.column_stack((a, b, c))   # matrix [a b c]
sign_val = np.linalg.det(A_mat)      # NumPy to check sign
scalar_triple = math.copysign(magnitude, sign_val)
print("a · (b × c) =", scalar_triple)

# Image generation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def draw_vec(v, color, label):
    ax.quiver(0, 0, 0, v[0], v[1], v[2],
              color=color, arrow_length_ratio=0.1, label=label)

# Draw just the vectors
draw_vec(a, 'r', 'a')
draw_vec(b, 'g', 'b')
draw_vec(c, 'b', 'c')

# Set axes limits
lim = 6
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])
ax.set_zlim([-lim, lim])

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()

plt.title(f"Scalar triple product = {scalar_triple}")
plt.savefig("gram_triple_product.png", dpi=300)
plt.show()

