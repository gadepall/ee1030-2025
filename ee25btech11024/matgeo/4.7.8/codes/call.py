import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared object library
lib = ctypes.CDLL("./find_shortest_distance.so")

# Define argument and return types
lib.find_shortest_distance.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, shape=(3,)),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, shape=(3,)),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, shape=(3,)),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, shape=(3,)),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, shape=(3,)),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, shape=(3,))
]
lib.find_shortest_distance.restype = ctypes.c_double

# --- Inputs ---
A_start = np.array([1, 1, 0], dtype=np.float64)
m1 = np.array([2, -1, 1], dtype=np.float64)
B_start = np.array([2, 1, -1], dtype=np.float64)
m2 = np.array([3, -5, 2], dtype=np.float64)

# Output arrays
pointA = np.zeros(3, dtype=np.float64)
pointB = np.zeros(3, dtype=np.float64)

# --- Call the C function ---
dist = lib.find_shortest_distance(A_start, m1, B_start, m2, pointA, pointB)
print(f"Shortest distance = {dist:.3f}")
print("Closest point on L1 (A):", pointA)
print("Closest point on L2 (B):", pointB)

# --- Plotting ---
kappa_range = np.linspace(-3, 3, 100)
mu_range = np.linspace(-3, 3, 100)

L1_points = np.array([A_start + k * m1 for k in kappa_range])
L2_points = np.array([B_start + k * m2 for k in mu_range])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot lines
ax.plot(L1_points[:,0], L1_points[:,1], L1_points[:,2], 'b', label='L1')
ax.plot(L2_points[:,0], L2_points[:,1], L2_points[:,2], 'orange', label='L2')

# Plot shortest distance line
ax.plot([pointA[0], pointB[0]], [pointA[1], pointB[1]], [pointA[2], pointB[2]],
        'g', linewidth=2, label='Shortest distance')

# Mark points
ax.scatter(*pointA, color='b')
ax.scatter(*pointB, color='orange')
ax.text(*pointA +0.5, "A", fontsize=10, color='b')
ax.text(*pointB - 1.0, "B", fontsize=10, color='orange')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Shortest Distance Between Two Skew Lines ")
plt.savefig("fig_call.png", dpi=300)
plt.show()
