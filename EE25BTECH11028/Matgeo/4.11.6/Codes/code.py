import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Plane: y - 3z + 6 = 0  => y = 3z - 6
# Create grid for plane
z = np.linspace(-5, 5, 20)
x = np.linspace(-5, 5, 20)
X, Z = np.meshgrid(x, z)
Y = 3*Z - 6

# Create figure
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# Plot plane
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan', rstride=1, cstride=1, edgecolor='k')

# Plot X-axis (y=0, z=0)
ax.plot([-5,5],[0,0],[0,0], color='red', linewidth=2, label='X-axis')

# Point on X-axis (origin)
origin = np.array([0,0,0])

# Distance point on plane from origin (perpendicular foot)
# Plane: 0*x + 1*y - 3*z + 6 = 0 => normal = (0,1,-3)
normal = np.array([0,1,-3])
d = 6
# Formula for projection of origin onto plane
t = -(np.dot(normal, origin) + d) / np.dot(normal, normal)
foot = origin + t*normal

# Plot perpendicular distance line
ax.plot([origin[0], foot[0]], [origin[1], foot[1]], [origin[2], foot[2]],
        color='green', linewidth=2, label='Shortest Distance')

# Plot origin and foot point
ax.scatter(*origin, color='red', s=50, label='Origin (on X-axis)')
ax.scatter(*foot, color='blue', s=50, label='Foot of perpendicular')

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Plane y - 3z + 6 = 0 and Distance from X-axis')
ax.legend()
plt.savefig ("fig8.png") 
plt.show()