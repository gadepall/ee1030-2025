# main.py
import os
import numpy as np
import ctypes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the C shared library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "function.so"))
lib.shortest_distance.restype = ctypes.c_double
lib.shortest_distance.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

# Define points/direction as doubles
p1 = np.array([2.0, 3.0, 2.0], dtype=np.double)
p2 = np.array([-2.0, 3.0, 0.0], dtype=np.double)
v  = np.array([2.0, -3.0, 6.0], dtype=np.double)

# Call the C function
dist = lib.shortest_distance(
    p1.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    p2.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    v.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)
print(f"Shortest distance = {dist:.4f}")

# Compute the closest points for plotting
w = p2 - p1
proj_len = np.dot(w, v) / np.dot(v, v)
closest_on_l1 = p1 + proj_len * v
closest_on_l2 = p2 + proj_len * v

# Plot both lines and the red perpendicular
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u_vals = np.linspace(-2, 2, 50)
l1_points = p1[:, None] + v[:, None] * u_vals
l2_points = p2[:, None] + v[:, None] * u_vals
ax.plot(l1_points[0], l1_points[1], l1_points[2], 'b', label='Line 1')
ax.plot(l2_points[0], l2_points[1], l2_points[2], 'g', label='Line 2')
ax.plot(
    [closest_on_l1[0], closest_on_l2[0]],
    [closest_on_l1[1], closest_on_l2[1]],
    [closest_on_l1[2], closest_on_l2[2]],
    'r', linewidth=2, label='Shortest Distance'
)
ax.view_init(elev=20, azim=45)
ax.legend()

# Save figure to ../figures
save_dir = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, "shortest_distance_c.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")
print("Image saved to:", os.path.abspath(save_path))

