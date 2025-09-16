import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the C library
lib = ctypes.CDLL("./function.so")

# Define function signature
lib.angle_between_lines.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.angle_between_lines.restype = ctypes.c_double

# Input lines
P1 = np.array([-3, 1, -3], dtype=float)   # Point on L1
d1 = np.array([3, 5, 4], dtype=float)     # Direction of L1

P2 = np.array([-1, 4, -5], dtype=float)   # Point on L2
d2 = np.array([1, 1, 2], dtype=float)     # Direction of L2

# Convert numpy arrays to ctypes
v1_c = d1.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
v2_c = d2.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call C function
theta_rad = lib.angle_between_lines(v1_c, v2_c)
theta_deg = np.degrees(theta_rad)

print(f"Angle between lines = {theta_rad:.6f} radians")
print(f"Angle between lines = {theta_deg:.2f} degrees")

# --- Plotting ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameter range
t = np.linspace(-2, 2, 20)

# Line 1
L1_points = P1[:, None] + d1[:, None] * t
ax.plot(L1_points[0], L1_points[1], L1_points[2], label="Line 1", color="blue")

# Line 2
L2_points = P2[:, None] + d2[:, None] * t
ax.plot(L2_points[0], L2_points[1], L2_points[2], label="Line 2", color="red")

# Scatter start points
ax.scatter(*P1, color="blue", s=50)
ax.scatter(*P2, color="red", s=50)

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title(f"Angle = {theta_deg:.2f}°")

# Save figure
import os

# Build the path: one folder out (..), then into figures/
save_path = os.path.join("..", "figures", "lines3dnew.png")

plt.savefig(save_path, dpi=150)

plt.show()

