import numpy as np
import matplotlib.pyplot as plt

# Define mutually perpendicular vectors
a = np.array([3, 0, 0])
b = np.array([0, 4, 0])
c = np.array([0, 0, 5])
s = a + b + c   # resultant (3,4,5)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot main vectors
ax.quiver(0, 0, 0, *a, color='r', linewidth=2,
          arrow_length_ratio=0.08, normalize=False, label='a (3)')
ax.quiver(0, 0, 0, *b, color='g', linewidth=2,
          arrow_length_ratio=0.08, normalize=False, label='b (4)')
ax.quiver(0, 0, 0, *c, color='b', linewidth=2,
          arrow_length_ratio=0.08, normalize=False, label='c (5)')

# Plot resultant
ax.quiver(0, 0, 0, *s, color='m', linewidth=2,
          arrow_length_ratio=0.05, normalize=False,
          label='a+b+c')

# Axis limits
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_zlim(0, 8)

# Axis labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Mutually Perpendicular Vectors and their Resultant")

ax.legend()
plt.show()




