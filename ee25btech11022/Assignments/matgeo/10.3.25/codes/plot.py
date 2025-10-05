# plot.py
import numpy as np
import matplotlib.pyplot as plt
from call import points

# Hyperbola: y = -2/(x-3)
x = np.linspace(-2, 8, 400)
with np.errstate(divide='ignore'):
    y = -2 / (x - 3)

valid = np.abs(x - 3) > 1e-8  # exclude singularity
x_h = x[valid]
y_h = y[valid]

fig, ax = plt.subplots(figsize=(8, 6))

# Plot hyperbola
ax.plot(x_h, y_h, 'r', label='Hyperbola')

# Tangents: x - 0.5 y = 5 -> y = 2x - 10, x - 0.5 y = 1 -> y = 2x - 2
x_vals = np.linspace(-2, 8, 400)
ax.plot(x_vals, 2 * x_vals - 10, 'orange', label='Tangent: $x - 0.5y = 5$')
ax.plot(x_vals, 2 * x_vals - 2, 'blue', label='Tangent: $x - 0.5y = 1$')

# Points of contact from C
ax.scatter(points[:, 0], points[:, 1], color='black', zorder=5, s=75, label='Points of contact')

for i, (x_c, y_c) in enumerate(points):
    ax.annotate(f'P{i+1} ({x_c:.1f}, {y_c:.1f})', (x_c, y_c), textcoords='offset points', xytext=(7,7), ha='left')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Tangents to the Curve')
ax.set_xlim(-2, 8)
ax.set_ylim(-10, 10)
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig('tangents.png', dpi=300)
plt.show()

