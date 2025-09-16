import sys
sys.path.insert(0, '/home/anshu-ram/matgeo/codes/CoordGeo')  # adjust path if needed

import numpy as np
import matplotlib.pyplot as plt

# local imports (from your CoordGeo library)
from line.funcs import line_gen

# -------------------------
# Step 1: Define vectors
# -------------------------
# Direction vector of line
v = np.array([1, -1, 0]).reshape(-1,1)

# Y-axis unit vector
e2 = np.array([0, 1, 0]).reshape(-1,1)

# -------------------------
# Step 2: Compute angle
# -------------------------
dot = float(v.T @ e2)             # dot product
norm_v = np.linalg.norm(v)        # ||v||
norm_e2 = np.linalg.norm(e2)      # ||e2||
cos_theta = dot / (norm_v*norm_e2)
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

print(f"Angle with Y-axis = {theta_deg:.2f} degrees")

# -------------------------
# Step 3: Plot using CoordGeo helpers
# -------------------------
# Generate line points
A = np.zeros((3,1))   # origin
B = v                 # point in direction of v
line_points = line_gen(A, B)      # line through origin in direction v

# Y-axis line
Y_end = np.array([0,2,0]).reshape(-1,1)
yaxis_points = line_gen(A, Y_end)

# Plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot line
ax.plot(line_points[0,:], line_points[1,:], line_points[2,:], label="Line (1,-1,0)", color="blue")

# Plot Y-axis
ax.plot(yaxis_points[0,:], yaxis_points[1,:], yaxis_points[2,:], label="Y-axis", color="green")

# Mark origin
ax.scatter(0,0,0, color="red", s=50)
ax.text(0,0,0,"O",fontsize=10)

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.title("Line vs Y-axis (Pure Python)")
plt.savefig("../figs/line.png")
plt.show()

