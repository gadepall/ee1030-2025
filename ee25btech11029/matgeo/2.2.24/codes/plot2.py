import numpy as np
import matplotlib.pyplot as plt

# Define the square vertices
points = np.array([
    [1, 7],   # A
    [4, 2],   # B
    [-1, -1], # C
    [-4, 4]   # D
])

# Close the square (repeat first point)
points = np.vstack([points, points[0]])

# Plot
plt.plot(points[:,0], points[:,1], "bo-", linewidth=2)
plt.title("Square of 4 Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.savefig('figs/square2.png')
plt.show()
