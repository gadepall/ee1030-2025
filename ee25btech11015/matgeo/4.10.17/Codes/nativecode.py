import numpy as np
import matplotlib.pyplot as plt

# Triangle vertices (computed from intersections of the lines)
vertices = np.array([
    [0.0, 1.0],   # Intersection of x + 2y = 2 and y - x = 1
    [2.0, 3.0],   # Intersection of y - x = 1 and 2x + y = 7
    [3.0, -0.5]   # Intersection of x + 2y = 2 and 2x + y = 7
])

# Plot the triangle
plt.figure(figsize=(6,6))
plt.fill(vertices[:,0], vertices[:,1], color='lightblue', alpha=0.5, label='Triangle Area')
plt.scatter(vertices[:,0], vertices[:,1], color='red')

# Label vertices
for i, (x, y) in enumerate(vertices):
    plt.text(x + 0.1, y + 0.1, f'V{i+1} ({x},{y})')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle formed by intersection of lines')
plt.grid(True)
plt.legend()
plt.show()
