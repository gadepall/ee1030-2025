import numpy as np
import matplotlib.pyplot as plt

# Coordinates of vertices
A = np.array([2, 5])
B = np.array([4, 7])
C = np.array([6, 2])

# Plot the triangle
fig, ax = plt.subplots()
triangle = plt.Polygon([A, B, C], fill=None, edgecolor='blue')
ax.add_patch(triangle)

# Scatter the points
ax.scatter(*A, color='red')
ax.scatter(*B, color='green')
ax.scatter(*C, color='orange')

# Annotate points
ax.annotate("A(2,5)", A, textcoords="offset points", xytext=(-15,5), ha='center')
ax.annotate("B(4,7)", B, textcoords="offset points", xytext=(10,5), ha='center')
ax.annotate("C(6,2)", C, textcoords="offset points", xytext=(10,-10), ha='center')

# Axes and labels
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_title("Triangle ABC")

# Equal aspect ratio and grid
ax.set_aspect('equal')
ax.grid(True)

plt.show()
