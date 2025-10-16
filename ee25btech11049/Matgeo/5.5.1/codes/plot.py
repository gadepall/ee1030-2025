import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# --- Calculations based on the image ---

# Define the matrices A and B from the system of equations AX = B
A = np.array([
    [5, -1, 4],
    [2, 3, 5],
    [5, -2, 6]
])

B = np.array([5, 2, -1])

# Calculate the inverse of A and the solution X
# X = [x, y, z]
try:
    A_inv = np.linalg.inv(A)
    X_solution = A_inv @ B
    x_int, y_int, z_int = X_solution
    print(f"The inverse of A is:\n{A_inv}\n")
    print(f"The solution is x={x_int}, y={y_int}, z={z_int}")
except np.linalg.LinAlgError:
    print("Matrix A is singular and does not have an inverse.")
    exit()

# --- Visualization ---

# Define the plane equations by solving for z
# 5x - y + 4z = 5  =>  z = (5 - 5x + y) / 4
def plane1(x, y):
    return (5 - 5*x + y) / 4

# 2x + 3y + 5z = 2  =>  z = (2 - 2x - 3y) / 5
def plane2(x, y):
    return (2 - 2*x - 3*y) / 5

# 5x - 2y + 6z = -1 =>  z = (-1 - 5x + 2y) / 6
def plane3(x, y):
    return (-1 - 5*x + 2*y) / 6

# Create a grid for plotting
x = np.linspace(-2, 8, 50)
y = np.linspace(-2, 8, 50)
X_grid, Y_grid = np.meshgrid(x, y)

Z1 = plane1(X_grid, Y_grid)
Z2 = plane2(X_grid, Y_grid)
Z3 = plane3(X_grid, Y_grid)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the three planes
ax.plot_surface(X_grid, Y_grid, Z1, alpha=0.5, color='red')
ax.plot_surface(X_grid, Y_grid, Z2, alpha=0.5, color='green')
ax.plot_surface(X_grid, Y_grid, Z3, alpha=0.5, color='blue')

# Plot the calculated intersection point
ax.scatter(x_int, y_int, z_int, color='black', s=150, label='Intersection Point', depthshade=False, zorder=10)
# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Three Planes')

# Create a custom legend for the planes and point
legend_elements = [
    Line2D([0], [0], color='red', lw=4, label='5x - y + 4z = 5'),
    Line2D([0], [0], color='green', lw=4, label='2x + 3y + 5z = 2'),
    Line2D([0], [0], color='blue', lw=4, label='5x - 2y + 6z = -1'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=10, label=f'Intersection: ({x_int:.0f}, {y_int:.0f}, {z_int:.0f})')
]
ax.legend(handles=legend_elements)

plt.show()
