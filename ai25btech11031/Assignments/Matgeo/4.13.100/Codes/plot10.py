import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define normal vector and plane constant
n = np.array([1, 1, 1])
d = 1

# Define points Q and S
Q = np.array([10, 15, 20])
S = np.array([-58/3, -43/3, -28/3])

# Create meshgrid for the plane
xx, yy = np.meshgrid(np.linspace(-10, 12, 30),
                     np.linspace(-10, 12, 30))
zz = (d - xx - yy)

# Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan', rstride=100, cstride=100)

# Plot points Q and S
ax.scatter(*Q, color='red', s=80, label='Q (10,15,20)')
ax.scatter(*S, color='blue', s=80, label='S (Reflection)')

# Draw line segment between Q and S
ax.plot([Q[0], S[0]], [Q[1], S[1]], [Q[2], S[2]], color='black', linestyle='--')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Reflection of Q across the plane x+y+z=1")
ax.legend()

plt.show()

