import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given vectors
a = np.array([1, 1, 1])
b = np.array([1, 2, 3])
sum_vec = a + b
diff_vec = a - b

# Cross product to find perpendicular unit vector to both (a+b) and (a-b)
cross = np.cross(sum_vec, diff_vec)
mag = np.linalg.norm(cross)

if mag == 0:
    raise ValueError("Vectors are parallel; no unique perpendicular vector.")

unit_pos = cross / mag
unit_neg = -unit_pos

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = np.zeros(3)

# Plot vectors a+b and a-b
ax.quiver(*origin, *sum_vec, color='b', label="a + b")
ax.quiver(*origin, *diff_vec, color='g', label="a - b")

# Plot positive and negative perpendicular unit vectors
ax.quiver(*origin, *unit_pos, color='m', label="Perp unit vector +")
ax.quiver(*origin, *unit_neg, color='c', label="Perp unit vector -")

# Set limits and labels
ax.set_xlim([min(0, -2), max(4, 4)])
ax.set_ylim([min(0, -2), max(4, 4)])
ax.set_zlim([min(0, -2), max(4, 4)])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title('3D plot of (a+b), (a-b) and perpendicular unit vectors')
plt.show()

