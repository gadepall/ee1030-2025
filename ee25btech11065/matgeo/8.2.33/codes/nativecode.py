import numpy as np
import matplotlib.pyplot as plt

a = 13
b = 12
c = 5

theta = np.linspace(0, 2 * np.pi, 200)

x = a * np.cos(theta)
y = b * np.sin(theta)

plt.figure(figsize=(10, 8))
ax = plt.gca()

ax.plot(x, y, label='Ellipse: $x^2/169 + y^2/144 = 1$')

ax.plot(0, 0, 'ko', label='Center (0, 0)')
ax.plot(c, 0, 'ro', label='Focus 1 (5, 0)')
ax.plot(-c, 0, 'ro', label='Focus 2 (-5, 0)')

ax.set_title('Plot of the Ellipse', fontsize=16)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.set_aspect('equal', adjustable='box')

ax.grid(True, linestyle='--')
ax.legend()

ax.set_xlim(-a - 2, a + 2)
ax.set_ylim(-b - 2, b + 2)

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

plt.show()


