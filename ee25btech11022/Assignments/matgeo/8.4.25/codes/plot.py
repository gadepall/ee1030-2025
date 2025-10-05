import numpy as np
import matplotlib.pyplot as plt
from call import get_data

vertex, p, directrix_x = get_data()

# Generate parabola points from equation transformed for y in terms of x
# From (y+2)^2 = -4(x - 0.5)
x = np.linspace(vertex[0] - 3, vertex[0] + 3, 400)
y_right = np.sqrt(-4 * (x - vertex[0])) - 2
y_left = -np.sqrt(-4 * (x - vertex[0])) - 2

fig, ax = plt.subplots(figsize=(8, 6))

# Plot parabola branches
ax.plot(x, y_right, 'r', label='Parabola branch')
ax.plot(x, y_left, 'r')

# Plot vertex
ax.plot(vertex[0], vertex[1], 'bo', label='Vertex')

# Plot directrix line: vertical line at x = directrix_x
ax.axvline(directrix_x, color='g', linestyle='--', linewidth=2, label=f'Directrix (x = {directrix_x:.2f})')

ax.set_xlim(vertex[0] - 4, vertex[0] + 4)
ax.set_ylim(vertex[1] - 4, vertex[1] + 4)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title('Plot of Parabola and Directrix')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
plt.show()

