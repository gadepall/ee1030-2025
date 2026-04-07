import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of values for Y and Z (Materials 2 and 3)
y = np.linspace(0, 10, 20)
z = np.linspace(0, 10, 20)
Y, Z = np.meshgrid(y, z)

# The boundary condition: x = y + z (which is x = 0.5(x + y + z))
X_boundary = Y + Z

# Setup the figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Plot the Boundary Plane
surf = ax.plot_surface(X_boundary, Y, Z, alpha=0.5, cmap='viridis', edgecolor='none')

# 2. Visualize the Feasible Region (Constraint)
# We generate random points and keep only those where x <= y + z
x_pts = np.random.uniform(0, 20, 5000)
y_pts = np.random.uniform(0, 10, 5000)
z_pts = np.random.uniform(0, 10, 5000)

# Filter points that satisfy the constraint: x <= 0.5(x + y + z)
mask = x_pts <= (y_pts + z_pts)
x = np.linspace(0, 20, 30)
y = np.linspace(0, 10, 30)
z = np.linspace(0, 10, 30)

X, Y, Z = np.meshgrid(x, y, z)

mask = X <= (Y + Z)

ax.scatter(X[mask], Y[mask], Z[mask],
           color='green', s=2, alpha=0.2)

# Labels and Title
ax.set_xlabel('Amount of X (Material 1)')
ax.set_ylabel('Amount of Y (Material 2)')
ax.set_zlabel('Amount of Z (Material 3)')
ax.set_title('Constraint Region: x $\leq$ 0.5(x + y + z)')

plt.show()