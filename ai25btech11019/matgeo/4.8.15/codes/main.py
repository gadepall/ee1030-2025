import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
# Remove toolbar: use plt.show() in scripts; in Jupyter, set %matplotlib inline.
# For saved images, toolbar is not included.

ax = fig.add_subplot(111, projection='3d')

t = np.linspace(-10, 10, 200)

# Thin lines: linewidth=2 for clarity (adjust to 1 if you want even thinner)
ax.plot(1 + t, 1 + 2*t, -1 + 3*t, color='blue', linewidth=2, label='Line 1')
ax.plot(-2 - 3*t, 2*t, 5*t, color='black', linewidth=2, label='Line 2')
ax.plot(-1 + 2*t, 3 - 7*t, -2 + 4*t, color='#8B0000', linewidth=2, label='Line l') # dark red

# Points: Crosses, clear and sized for visibility
ax.scatter(-1, 3, -2, color='red', marker='x', s=80, linewidths=3, label='Point on line l')
ax.scatter(1, 1, -1, color='blue', marker='x', s=80, linewidths=3, label='Point on line 1')
ax.scatter(-2, 0, 0, color='green', marker='x', s=80, linewidths=3, label='Point on line 2')
ax.scatter(0, 0, 0, color='black', marker='x', s=80, linewidths=3, label='Origin')

ax.set_xlabel('X', fontsize=11)
ax.set_ylabel('Y', fontsize=11)
ax.set_zlabel('Z', fontsize=11)
ax.set_title('3D Visualization of Lines', fontsize=14)
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 25)
ax.set_zlim(-10, 10)

# Legend in top right (corner) for best visibility and professional appearance
handles, labels = ax.get_legend_handles_labels()
from collections import OrderedDict
uniq = OrderedDict(zip(labels, handles))
ax.legend(uniq.values(), uniq.keys(), loc='upper right', fontsize=10, framealpha=1)

plt.tight_layout()
plt.show()
