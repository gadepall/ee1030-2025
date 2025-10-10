import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define the points ---
A = np.array([3, -2, -1])
B = np.array([2, 3, -4])
C = np.array([-1, 1, 2])
# The given value for lambda
lam = -146 / 17 
D = np.array([4, 5, lam])

points = {'A': A, 'B': B, 'C': C, 'D': D}

# --- 2. Calculate the equation of the plane from A, B, and C ---
# Create two vectors on the plane
vec1 = B - A
vec2 = C - A

# The normal vector is the cross product of the two vectors
normal = np.cross(vec1, vec2)

# Plane equation is: a*x + b*y + c*z + d = 0, where (a,b,c) is the normal vector
# We find d by plugging in one of the points (e.g., A)
a, b, c = normal
d = -np.dot(normal, A)

# --- 3. Create a grid of points to plot the plane surface ---
# Create a grid slightly larger than the min/max of our points
all_points = np.array([A, B, C, D])
x_min, x_max = all_points[:, 0].min(), all_points[:, 0].max()
y_min, y_max = all_points[:, 1].min(), all_points[:, 1].max()

x_range = np.linspace(x_min - 2, x_max + 2, 20)
y_range = np.linspace(y_min - 2, y_max + 2, 20)
xx, yy = np.meshgrid(x_range, y_range)

# Calculate the corresponding z value for each (x, y) point on the plane
# a*x + b*y + c*z + d = 0  =>  z = (-a*x - b*y - d) / c
zz = (-a * xx - b * yy - d) / c

# --- 4. Plotting ---
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane surface (with transparency)
ax.plot_surface(xx, yy, zz, alpha=0.4, color='cyan', rstride=100, cstride=100)

# Plot and label each point
for name, p in points.items():
    # Plot the point
    ax.scatter(p[0], p[1], p[2], color='red', s=60, depthshade=True)
    # Create the label text with name and coordinates (rounded to 2 decimal places)
    label = f' {name} ({p[0]:.2f}, {p[1]:.2f}, {p[2]:.2f})'
    # Add the text label next to the point
    ax.text(p[0], p[1], p[2], label, size=11, zorder=1, color='k')

# --- 5. Formatting the plot ---
ax.set_xlabel('X-axis', fontweight='bold')
ax.set_ylabel('Y-axis', fontweight='bold')
ax.set_zlabel('Z-axis', fontweight='bold')
ax.set_title('3D Plot of Coplanar Points and Plane', fontsize=16)
plt.savefig('2.png')
plt.show()