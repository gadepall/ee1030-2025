import numpy as np
import matplotlib.pyplot as plt
from call import get_data_from_c

P, curve_points = get_data_from_c()
slope = 2.0 / 3.0
x_tangent = np.array([0, 8])
y_tangent = slope * (x_tangent - P[0]) + P[1]
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(curve_points[:, 0], curve_points[:, 1], 'b-', linewidth=2.5, label='Curve: $y = \\sqrt{4x-3} - 1$')

ax.plot(x_tangent, y_tangent, 'g--', label='Tangent Line')

ax.scatter(P[0], P[1], color='red', s=100, zorder=5)
ax.text(P[0] + 0.2, P[1] , f'P({P[0]:.0f}, {P[1]:.0f})')

ax.set_title('Tangent to the Curve',fontsize=14)
ax.set_xlabel('X-axis',fontsize=14)
ax.set_ylabel('Y-axis',fontsize=14)
ax.set_xlim(0, 8)
ax.set_ylim(-1.5, 5)

ax.grid(True)
ax.legend(fontsize=12)

plt.show()
plt.savefig('fig.png')
