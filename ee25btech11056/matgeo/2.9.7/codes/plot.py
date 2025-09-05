import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vectors
a = np.array([2,1,3])
b = np.array([-1,2,1])
c = np.array([3,1,2])

# Gram matrix
G = np.array([
    [np.dot(a,a), np.dot(a,b), np.dot(a,c)],
    [np.dot(b,a), np.dot(b,b), np.dot(b,c)],
    [np.dot(c,a), np.dot(c,b), np.dot(c,c)]
])

# Determinant and box product
detG = np.linalg.det(G)
box = -np.sqrt(detG)

print("Determinant of Gram matrix =", detG)
print("Box product =", box)

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = np.array([0,0,0])

# Plot vectors
ax.quiver(*origin, *a, color='r', arrow_length_ratio=0.1, label="a = (2,1,3)")
ax.quiver(*origin, *b, color='g', arrow_length_ratio=0.1, label="b = (-1,2,1)")
ax.quiver(*origin, *c, color='b', arrow_length_ratio=0.1, label="c = (3,1,2)")

ax.set_xlim([-2,4])
ax.set_ylim([-2,4])
ax.set_zlim([0,4])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Vectors a, b, c (Box product = {box:.2f})")
ax.legend()

plt.savefig("vectors.png")
plt.show()

