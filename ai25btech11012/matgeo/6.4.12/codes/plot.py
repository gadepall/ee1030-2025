# Code by Unnathi Garige
# Plots two parametric lines x1 and x2 in 3D

import numpy as np
import matplotlib.pyplot as plt

# Function to generate parametric line points
def line_param(P, d, t_vals):
    return np.array([P + t * d for t in t_vals]).T

# Line 1: x1 = [1,2,1] + λ [1,-1,1]
P1 = np.array([1, 2, 1])
d1 = np.array([1, -1, 1])

# Line 2: x2 = [2,-1,-1] + μ [2,-1,2]
P2 = np.array([2, -1, -1])
d2 = np.array([2, -1, 2])

# Parameter values
t_vals = np.linspace(-5, 5, 100)

# Generate points
x1 = line_param(P1, d1, t_vals)
x2 = line_param(P2, d2, t_vals)

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot lines
ax.plot(x1[0, :], x1[1, :], x1[2, :], color="red", label=r"$\vec{x_1}$")
ax.plot(x2[0, :], x2[1, :], x2[2, :], color="blue", label=r"$\vec{x_2}$")

# Mark starting points
ax.scatter(P1[0], P1[1], P1[2], color="black", marker="o")
ax.text(P1[0], P1[1], P1[2], "P1(1,2,1)", fontsize=10)

ax.scatter(P2[0], P2[1], P2[2], color="black", marker="o")
ax.text(P2[0], P2[1], P2[2], "P2(2,-1,-1)", fontsize=10)

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Parametric Lines in 3D")
ax.legend()
ax.grid(True)

# Save and Show
plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/6.4.12/figs/fig.png')
plt.show()

