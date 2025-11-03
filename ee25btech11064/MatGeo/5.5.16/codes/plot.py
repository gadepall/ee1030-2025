import numpy as np
import matplotlib.pyplot as plt

# Plane functions:
def plane1(x, y):
    return (11 - 2*x + 3*y) / 5

def plane2(x, y):
    return -(3*x - 2*y + 5) / 4

def plane3(x, y):
    return (x + y + 3) / 2

# Create grid
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

Z1 = plane1(X, Y)
Z2 = plane2(X, Y)
Z3 = plane3(X, Y)

# Intersection point
x_int = 27/35
y_int = -2/35
z_int = 13/7

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z1, alpha=0.5, color='red', label='2x - 3y + 5z = 11')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='green', label='3x - 2y - 4z = -5')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='blue', label='x + y - 2z = -3')

# Plot the intersection point
ax.scatter(x_int, y_int, z_int, color='black', s=100, label='Intersection Point')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Planes and their Intersection Point')

# Legend (manual, since plot_surface doesn't handle labels well)
from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color='red', lw=4),
                Line2D([0], [0], color='green', lw=4),
                Line2D([0], [0], color='blue', lw=4),
                Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=10)]
ax.legend(custom_lines, ['Plane 1: 2x - 3y + 5z = 11', 
                        'Plane 2: 3x - 2y - 4z = -5', 
                        'Plane 3: x + y - 2z = -3', 
                        'Intersection Point (27/35, -2/35, 13/7)'])

plt.show()

