import numpy as np
import matplotlib.pyplot as plt

# Given points
A = np.array([1, -2, 3])
B = np.array([3, 4, -5])

# Internal division (2:3)
P = (2*B + 3*A) / 5

# External division (2:3)
Q = (2*B - 3*A) / (2-3)

# Plotting projection in 2D (x-y plane)
plt.plot([A[0], B[0]], [A[1], B[1]], label='AB')

# Scatter points
points = np.array([A[:2], B[:2], P[:2], Q[:2]])
labels = ['A', 'B', 'P', 'Q']
for i, txt in enumerate(labels):
    plt.scatter(points[i,0], points[i,1], label=f"{txt}")
    plt.annotate(f'{txt}\n({points[i,0]:.1f}, {points[i,1]:.1f})',
                 (points[i,0], points[i,1]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes settings
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')

plt.savefig('figs/Plot_C.png')
plt.show()