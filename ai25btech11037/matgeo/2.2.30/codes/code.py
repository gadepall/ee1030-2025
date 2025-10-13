import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Line: (x+1)/2 = y/3 = (z-3)/6
# Direction ratios of line
d = np.array([2, 3, 6])

# Plane: 10x + 2y - 11z = 3
n = np.array([10, 2, -11])  # normal vector of plane

# Angle between line and plane
# angle θ = 90° - angle(line, normal)
cos_theta = abs(np.dot(d, n)) / (np.linalg.norm(d) * np.linalg.norm(n))
theta = np.arcsin(cos_theta)  # angle between line and plane in radians
theta_deg = np.degrees(theta)

print("Angle between line and plane = ", theta_deg, "degrees")

# ---------- Plotting ----------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create grid for plane
xx, yy = np.meshgrid(range(-5, 6), range(-5, 6))
zz = (10*xx + 2*yy - 3) / 11  # from plane equation

# Plot plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Line parametric form: x = -1 + 2t, y = 3t, z = 3 + 6t
t = np.linspace(-2, 2, 50)
x_line = -1 + 2*t
y_line = 3*t
z_line = 3 + 6*t

# Plot line
ax.plot(x_line, y_line, z_line, color='red', linewidth=2, label="Line")

# Formatting
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f"Angle = {theta_deg:.2f}°")
ax.legend()

# Save the figure
plt.savefig("line_plane_angle.png", dpi=300)
plt.show()
