import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Coordinates of points P and Q
Px, Py, Pz = 4, 3, -5
Qx, Qy, Qz = -2, 1, -8

# Direction vector PQ = Q - P
dx = Qx - Px
dy = Qy - Py
dz = Qz - Pz

# Magnitude of PQ
magnitude = np.sqrt(dx**2 + dy**2 + dz**2)

# Unit vector along the direction of PQ
ux = dx / magnitude
uy = dy / magnitude
uz = dz / magnitude

# Create a figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points P and Q
ax.scatter([Px, Qx], [Py, Qy], [Pz, Qz], color='red', label='Points P and Q')

# Plot the unit vector along PQ starting from P
ax.quiver(Px, Py, Pz, ux, uy, uz, length=3, color='blue', label='Unit Vector along PQ')

# Annotate the points P and Q
ax.text(Px, Py, Pz, 'P(4,3,-5)', color='black', fontsize=12)
ax.text(Qx, Qy, Qz, 'Q(-2,1,-8)', color='black', fontsize=12)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of Points P, Q and Unit Vector along PQ')

# Set grid and legend
ax.grid(True)
ax.legend()

# Save the figure as a PNG file
fig.savefig('direction_vector_plot.png', dpi=300)

# Show the plot
plt.show()

