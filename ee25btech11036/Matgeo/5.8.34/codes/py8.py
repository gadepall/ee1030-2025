import sys
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')  # your path

import numpy as np
import matplotlib.pyplot as plt

# local imports
from line.funcs import line_gen  # your line generation function

# Given lines:
# L1: x - y + 1 = 0 => y = x + 1
# L2: 3x + 2y - 12 = 0 => y = (12 - 3x)/2

# Find vertices of triangle formed by lines and axes:

# Intersection of L1 with x-axis (y=0): x - 0 + 1=0 => x=-1
A = np.array([-1, 0]).reshape(-1, 1)

# Intersection of L2 with x-axis (y=0): 3x - 12=0 => x=4
B = np.array([4, 0]).reshape(-1, 1)

# Intersection of L1 and L2: solve
# y = x + 1 and y = (12 - 3x)/2
# => x + 1 = (12 - 3x)/2 => 2x + 2 = 12 - 3x => 5x=10 => x=2, y=3
C = np.array([2, 3]).reshape(-1, 1)

# Generate triangle edges using your line_gen
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Plot original lines for reference
x_vals = np.linspace(-2, 5, 200)
y_L1 = x_vals + 1
y_L2 = (12 - 3 * x_vals) / 2

plt.plot(x_vals, y_L1, 'r--', label='$x - y + 1 = 0$')
plt.plot(x_vals, y_L2, 'g--', label='$3x + 2y - 12 = 0$')

# Plot axes
plt.axhline(0, color='black')  # x-axis
plt.axvline(0, color='black')  # y-axis

# Plot triangle edges
plt.plot(x_AB[0, :], x_AB[1, :], 'b-', linewidth=2, label='Triangle edges')
plt.plot(x_BC[0, :], x_BC[1, :], 'b-', linewidth=2)
plt.plot(x_CA[0, :], x_CA[1, :], 'b-', linewidth=2)

# Fill triangle
plt.fill([A[0,0], B[0,0], C[0,0]], [A[1,0], B[1,0], C[1,0]], 'skyblue', alpha=0.5)

# Label points
points = np.hstack((A, B, C))
labels = ['A', 'B', 'C']
for i, txt in enumerate(labels):
    plt.scatter(points[0, i], points[1, i], color='black')
    plt.annotate(f'{txt}\n({points[0, i]:.2f}, {points[1, i]:.2f})',
                 (points[0, i], points[1, i]),
                 textcoords="offset points",
                 xytext=(15, 5),
                 ha='center')

# Axis formatting same as your code
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.grid(True)
plt.axis('equal')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Triangle formed by given lines and axes')
plt.legend(loc='best')

plt.show()

