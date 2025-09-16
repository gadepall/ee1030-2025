import numpy as np
import matplotlib.pyplot as plt

def get_z(x, y):
    return (12 - 6*x - 4*y) / 3

x_vals = np.linspace(0, 4, 10)
y_vals = np.linspace(0, 5, 10)
x_grid, y_grid = np.meshgrid(x_vals, y_vals)
z_grid = get_z(x_grid, y_grid)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.7, cmap='viridis')

ax.scatter(2, 0, 0, color='red', s=100, label='Intercept (2,0,0)')
ax.scatter(0, 3, 0, color='green', s=100, label='Intercept (0,3,0)')
ax.scatter(0, 0, 4, color='blue', s=100, label='Intercept (0,0,4)')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Plane: 6x + 4y + 3z = 12')
ax.legend()
plt.grid(True)
plt.show()


