import ctypes, os, math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lib = ctypes.CDLL("./prob2.so")

# Function signature
lib.unit_vector_3d.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
]
lib.unit_vector_3d.restype = ctypes.c_int

def unit_vector_from_c(P, Q):
    P_arr = (ctypes.c_double * 3)(*P)
    Q_arr = (ctypes.c_double * 3)(*Q)
    U_arr = (ctypes.c_double * 3)()
    ret = lib.unit_vector_3d(P_arr, Q_arr, U_arr)
    if ret != 0:
        raise ValueError("P and Q coincide.")
    return [U_arr[0], U_arr[1], U_arr[2]]

# Example points
P = (1.0, 2.0, 3.0)
Q = (4.0, 5.0, 6.0)

# Get unit vector
u = unit_vector_from_c(P, Q)
PQ = [Q[i]-P[i] for i in range(3)]
print("Unit vector:", u)

# --- Plot ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*P, color="red", s=60, label="P")
ax.scatter(*Q, color="blue", s=60, label="Q")

# Vector PQ
ax.quiver(P[0], P[1], P[2], PQ[0], PQ[1], PQ[2], color="green", label="PQ")

# Unit vector (length 1)
ax.quiver(P[0], P[1], P[2], u[0], u[1], u[2], color="orange", label="Unit vector")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()

