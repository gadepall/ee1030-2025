import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter ranges
lambda_vals = np.linspace(-1.5, 1, 100)
mu_vals = np.linspace(-2.5, 1, 100)

# Line 1: r = (8 + 3λ) i - (9 + 16λ) j + (10 + 7λ) k
x1 = 8 + 3 * lambda_vals
y1 = -9 - 16 * lambda_vals
z1 = 10 + 7 * lambda_vals

# Line 2: r = 15i + 29j + 5k + μ(3i + 8j - 5k)
x2 = 15 + 3 * mu_vals
y2 = 29 + 8 * mu_vals
z2 = 5 - 5 * mu_vals

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot Line 1
ax.plot(x1, y1, z1, label='Line 1', color='blue', linewidth=2)

# Plot Line 2
ax.plot(x2, y2, z2, label='Line 2', color='red', linewidth=2)

# Shortest distance segment as thin dashed green line
S1 = np.array([5., 7., 3.])
S2 = np.array([9., 13., 15.])
ax.plot([S1[0], S2[0]], [S1[1], S2[1]], [S1[2], S2[2]],
        color='green', linestyle='--', linewidth=1, label='Shortest Segment')

# Axes labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('3D Plot of Lines and Shortest Distance Segment')
plt.savefig('shortest_distance_3d.png', dpi=300, bbox_inches='tight')
plt.show()

