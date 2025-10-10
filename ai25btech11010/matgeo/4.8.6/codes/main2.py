import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os


# Load the shared library (use absolute path if needed)
lib = ctypes.CDLL("./main.so")  # or absolute path

# Prepare point P and normal n
P_vals = [3.0, 2.0, 1.0]
n_vals = [2.0, -1.0, 1.0]

# Allocate pointers for P and n (double**)
P = (ctypes.POINTER(ctypes.c_double) * 3)()
n = (ctypes.POINTER(ctypes.c_double) * 3)()
for i in range(3):
    P[i] = ctypes.pointer(ctypes.c_double(P_vals[i]))
    n[i] = ctypes.pointer(ctypes.c_double(n_vals[i]))

# Prepare outputs
distance = ctypes.c_double()
R = (ctypes.c_double * 3)()

# Call the C function
lib.point_plane_info(
    P,                 # double**
    n,                 # double**
    ctypes.c_double(-1.0),  # plane constant d
    ctypes.byref(distance),  # double* output
    R                  # double* output
)

# Convert R to numpy array
R_vals = np.array([R[i] for i in range(3)])
P_arr = np.array(P_vals)
n_arr = np.array(n_vals)
d = -1.0

# Compute Q = foot of perpendicular
lam = (np.dot(n_arr, P_arr) - d) / np.dot(n_arr, n_arr)
Q_arr = P_arr - lam * n_arr

# Print results
print("Distance from P to plane:", distance.value)
print("Foot of perpendicular Q:", Q_arr)
print("Reflection R:", R_vals)

# --- Plotting ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points P, Q, R
ax.scatter(*P_arr, color='blue', label='P')
ax.scatter(*Q_arr, color='green', label='Q (foot)')
ax.scatter(*R_vals, color='red', label='R (reflection)')

# Plot plane
xx, yy = np.meshgrid(np.linspace(0,5,10), np.linspace(0,5,10))
zz = (-n_arr[0]*xx - n_arr[1]*yy + d)/n_arr[2]
ax.plot_surface(xx, yy, zz, alpha=0.3, color='orange')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Point, Foot of Perpendicular, Reflection, Plane")

# Save figure
plt.savefig("../figs/point_plane_plot.png", dpi=300)
plt.show()
