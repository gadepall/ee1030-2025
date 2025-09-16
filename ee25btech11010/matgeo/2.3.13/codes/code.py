import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, c_double

# Load the shared library
lib = CDLL("./code.so")  # use your code.so file

# Define argument and return types
lib.angleWithYAxis.argtypes = [c_double, c_double, c_double]
lib.angleWithYAxis.restype = c_double

# Vector
vx, vy, vz = 1.0, -1.0, 2.0

# Call C function
theta_deg = lib.angleWithYAxis(vx, vy, vz)
print(f"Angle with positive Y-axis = {theta_deg:.2f} degrees")

# 3D plotting
v = np.array([vx, vy, vz])
e2 = np.array([0, 1, 0])  # Y-axis unit vector

# Normalize for plotting
v_unit = v / np.linalg.norm(v)
e2_unit = e2 / np.linalg.norm(e2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
origin = np.array([0, 0, 0])

# Plot vectors
ax.quiver(*origin, *v_unit, color='r', length=1)
ax.quiver(*origin, *e2_unit, color='b', length=1)

# Labels
ax.text(*(v_unit + 0.1), f"Line {tuple(v)}", color='r', fontsize=10)
ax.text(*(e2_unit + 0.1), f"Y-axis {tuple(e2)}", color='b', fontsize=10)
ax.text(0.2, 0.2, 0.2, f"Angle with Y-axis: {theta_deg:.2f}°", color='k', fontsize=12)

# Axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 2])
ax.grid(True)

plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/2.3.13/figs/q3.png")

plt.show()
