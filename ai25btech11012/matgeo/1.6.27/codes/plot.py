# Code by Unnathi Garige
# Plots a line joining three points A, B, C in 3D

import numpy as np
import matplotlib.pyplot as plt

# Function to generate line points in 3D
def line_gen(A, B, n=50):
    dim = A.shape[0]
    x_AB = np.zeros((dim, n))
    lam = np.linspace(0, 1, n)
    for i in range(n):
        x_AB[:, i] = A + lam[i] * (B - A)
    return x_AB

# Points
A = np.array([-4, 6, 10])
B = np.array([2, 4, 6])
C = np.array([14, 0, -2])

# Generate line segments
xAB = line_gen(A, B)
xBC = line_gen(B, C)

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot lines
ax.plot(xAB[0, :], xAB[1, :], xAB[2, :], color="red", label='AB')
ax.plot(xBC[0, :], xBC[1, :], xBC[2, :], color="blue", label='BC')

# Scatter points
coords = np.vstack((A, B, C)).T
ax.scatter(coords[0, :], coords[1, :], coords[2, :], color="black")

# Labels
labels = ['A', 'B', 'C']
for i, txt in enumerate(labels):
    ax.text(coords[0, i], coords[1, i], coords[2, i], txt, fontsize=12)

# Axis labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Line joining points A, B, C")
ax.legend()
ax.grid(True)

# Save and Show
plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.6.27/figs')
plt.show()

