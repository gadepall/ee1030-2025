import numpy as np
import matplotlib.pyplot as plt

# Circle parameters
center = (1, 0)
radius = 2

# Circle points
theta = np.linspace(0, 2*np.pi, 400)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

# Points of tangency
A = (1, 2)
B = (1, -2)

# Tangents (horizontal lines through A and B)
x_tangent = np.linspace(-2, 4, 400)
y_tangent1 = np.full_like(x_tangent, A[1])  # y = 2
y_tangent2 = np.full_like(x_tangent, B[1])  # y = -2

# Plot the circle
plt.plot(x, y, 'g', label='Circle')

# Plot tangents
plt.plot(x_tangent, y_tangent1, 'b', label='Tangent 1')
plt.plot(x_tangent, y_tangent2, 'orange', label='Tangent 2')

# Mark and annotate points A and B
plt.scatter(*A, color='purple')
plt.text(A[0], A[1]+0.2, 'A', fontsize=12, ha='center')
plt.text(A[0], A[1]-0.3, f"({A[0]:.2f}, {A[1]:.2f})", ha='center')

plt.scatter(*B, color='yellow')
plt.text(B[0], B[1]-0.3, 'B', fontsize=12, ha='center')
plt.text(B[0], B[1]-0.6, f"({B[0]:.2f}, {B[1]:.2f})", ha='center')

# Axis formatting
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)

plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/10.7.21/figs/fig.png')

plt.show()

