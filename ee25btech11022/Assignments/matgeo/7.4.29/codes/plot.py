import matplotlib.pyplot as plt
import numpy as np
from call import get_data

c1, r1, c2, r2, chord_y = get_data()

fig, ax = plt.subplots(figsize=(7,7))

# Full circle 1 (center c1, radius r1)
circle1 = plt.Circle(c1, r1, color='r', fill=False, linewidth=2, label='Circle 1 (center (1,3), r=2)')

# Full circle 2 (center c2, radius r2)
circle2 = plt.Circle(c2, r2, color='b', fill=False, linewidth=2, label='Circle 2 (center (2,1), r=2)')

ax.add_artist(circle1)
ax.add_artist(circle2)

# Plot centers
ax.plot(c1[0], c1[1], 'ro', label='Center Circle 1')
ax.plot(c2[0], c2[1], 'bo', label='Center Circle 2')

# Plot chord line y = chord_y
x_vals = np.linspace(min(c1[0], c2[0]) - 3, max(c1[0], c2[0]) + 3, 400)
y_vals = np.full_like(x_vals, chord_y)
ax.plot(x_vals, y_vals, 'g--', linewidth=2, label=f'Chord line (y={chord_y})')

ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_xlim(min(c1[0], c2[0]) - 4, max(c1[0], c2[0]) + 4)
ax.set_ylim(min(c1[1], c2[1], chord_y) - 4, max(c1[1], c2[1], chord_y) + 4)
plt.title('Circles with intersection of chord as diameter')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

