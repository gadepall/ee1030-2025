import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./libparallelogram.so")

# Define return type for the intersection function
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

lib.intersection.restype = Point

# Get intersection P
P = lib.intersection()
print("Intersection P =", (P.x, P.y))

# Define points
O = np.array([0, 0])
A = np.array([1, 0])
B = np.array([0, 1])
C = A + B
D = (O + A)/2
P_vec = np.array([P.x, P.y])

# --- Plot ---
fig, ax = plt.subplots()

# Parallelogram
ax.plot([O[0], A[0], C[0], B[0], O[0]],
        [O[1], A[1], C[1], B[1], O[1]], 'k-')

# Diagonal OC
ax.plot([O[0], C[0]], [O[1], C[1]], 'r--', label="OC")
# Line BD
ax.plot([B[0], D[0]], [B[1], D[1]], 'g--', label="BD")

# Points
for Pnt, name in zip([O,A,B,C,D,P_vec], ['O','A','B','C','D','P']):
    ax.scatter(Pnt[0], Pnt[1], s=50)
    ax.text(Pnt[0]+0.05, Pnt[1]+0.05, name)

ax.set_aspect('equal')
ax.legend()
plt.title("Intersection of BD and CO in ratio 2:1")
plt.show()
