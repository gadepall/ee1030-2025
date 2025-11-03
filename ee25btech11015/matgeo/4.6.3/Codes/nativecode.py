import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Given line (reference line) ---
t = np.linspace(-5, 5, 100)

# Reference line passes through (-3,4,-8) with direction (3,5,6)
x1 = -3 + 3*t
y1 = 4 + 5*t
z1 = -8 + 6*t

# Required line passes through (-2,4,-5) with same direction (3,5,6)
x2 = -2 + 3*t
y2 = 4 + 5*t
z2 = -5 + 6*t

# --- Plot ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Plot reference line
ax.plot(x1, y1, z1, color="blue", label="Given Line")

# Plot required line
ax.plot(x2, y2, z2, color="red", linestyle="--", label="Required Line")

# Mark the given point P(-2,4,-5)
ax.scatter(-2,4,-5, color="green", s=50)
ax.text(-2,4,-5, "P(-2,4,-5)", color="green")

# Axes labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Line through P(-2,4,-5) parallel to given line")
ax.legend()
ax.grid(True)

plt.show()
