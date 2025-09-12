import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors OA and OB
OA = np.array([1, 2, 3])
OB = np.array([-3, 1, 1])
O = np.array([0, 0, 0])

# Create figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
plt.style.use('seaborn-v0_8')

# Plot vectors OA and OB
ax.quiver(*O, *OA, color='blue', arrow_length_ratio=0.1, label='Vector OA')
ax.quiver(*O, *OB, color='green', arrow_length_ratio=0.1, label='Vector OB')

# Define triangle vertices
triangle = np.array([O, OA, OB])

# Plot triangle surface
ax.plot_trisurf(triangle[:,0], triangle[:,1], triangle[:,2], color='lightblue', alpha=0.6)

# Annotate points
ax.text(*OA, 'A', fontsize=12, color='blue')
ax.text(*OB, 'B', fontsize=12, color='green')
ax.text(*O, 'O', fontsize=12, color='black')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Triangle OAB Formed by Vectors OA and OB')
ax.legend()

# Save plot
plt.title("Area of Triangle")
plt.grid(True)
plt.axis('equal')
plt.show()

print("3D plot of triangle OAB has been saved as 'triangle_OAB_3D_plot.png'.")

