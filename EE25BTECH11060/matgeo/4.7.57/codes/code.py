import numpy as np
import matplotlib.pyplot as plt

# Line: 3x - 4y - 26 = 0
n = np.array([3, -4])   # normal vector
c = 26
P = np.array([3, -5])   # given point

# Foot of perpendicular formula: Q = P - ((n^T P - c)/||n||^2) * n
dot = n @ P
Q = P - ((dot - c) / (np.dot(n, n))) * n

# Prepare line for plotting
x_vals = np.linspace(-10, 10, 400)
y_vals = (3*x_vals - 26)/4   # from 3x - 4y - 26 = 0

# Plot line
plt.plot(x_vals, y_vals, 'b', label=r'$3x-4y-26=0$')

# Plot point P
plt.scatter(P[0], P[1], color='red', zorder=5)
plt.text(P[0]+0.3, P[1]-0.3, 'P(3,-5)', fontsize=12, color='red')

# Plot foot of perpendicular Q
plt.scatter(Q[0], Q[1], color='green', zorder=5)
plt.text(Q[0]+0.3, Q[1]+0.3, f'Q({Q[0]:.2f},{Q[1]:.2f})', fontsize=12, color='green')

# Dotted line PQ
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'r--', label='Shortest Distance')

# Axes & labels
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.title("Distance from Point to Line")
plt.show()
