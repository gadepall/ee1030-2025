import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given vectors
a = np.array([1, 2, 5])
b = np.array([1, 2, -1])

# Vector c is parallel to 2i - j
c = np.array([2, -1, 0])

# Verify orthogonality (dot products)
dot_a_c = np.dot(a, c)
dot_b_c = np.dot(b, c)

print("a · c =", dot_a_c)
print("b · c =", dot_b_c)
print("\nSince both dot products are 0, c is orthogonal to both a and b.")
print("Hence, c is parallel to 2i - j.\n")

# Plot setup
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot vectors
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, c[0], c[1], c[2], color='g', arrow_length_ratio=0.1)

# Label each vector beside its arrow
ax.text(a[0]*1.05, a[1]*1.05, a[2]*1.05, 'a = i + 2j + 5k', color='r', fontsize=10)
ax.text(b[0]*1.05, b[1]*1.05, b[2]*1.05, 'b = i + 2j - k', color='b', fontsize=10)
ax.text(c[0]*1.05, c[1]*1.05, c[2]*1.05, 'c ∥ 2i - j', color='g', fontsize=10)

# Axis labels and style
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_xlim([-1, 5])
ax.set_ylim([-2, 5])
ax.set_zlim([-2, 6])
ax.set_title('Vectors a, b, and c (c ∥ 2i - j)')
ax.grid(True)

# Save the figure
plt.savefig("vectors_plot.png", dpi=300, bbox_inches='tight')
print("Figure saved as 'vectors_plot.png' successfully.")

# Show the plot
plt.show()

