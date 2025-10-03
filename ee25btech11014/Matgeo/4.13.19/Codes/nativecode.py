import numpy as np
import matplotlib.pyplot as plt

# Given points
A = np.array([1, 1])
B = np.array([2, 4])

# Ratio 3:2
m, n = 3, 2
P = np.array([(m*B[0] + n*A[0])/(m+n), (m*B[1] + n*A[1])/(m+n)])

# Line equation: 2x + y = 6  => y = 6 - 2x
x_vals = np.linspace(0, 3, 100)
y_vals = 6 - 2*x_vals

plt.figure(figsize=(6,6))

# Plot line segment AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'g--', label='Line Segment AB')

# Plot line 2x+y=6
plt.plot(x_vals, y_vals, 'b', label='Line: 2x + y = 6')

# Plot points
plt.scatter(*A, color='red', label='A(1,1)')
plt.scatter(*B, color='orange', label='B(2,4)')
plt.scatter(*P, color='purple', s=80, marker='o', label='P(1.6, 2.8)')

# Labels
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line passing through internal division point')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.axis("equal")

# Save the figure
plt.savefig("findk.png", dpi=300, bbox_inches='tight')
plt.show()
