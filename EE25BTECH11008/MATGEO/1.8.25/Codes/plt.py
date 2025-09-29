import numpy as np
import matplotlib.pyplot as plt

# Define points
A = np.array([7, 1])
B = np.array([3, 5])

# Define line y = x - 2
x_vals = np.linspace(0, 10, 100)
y_vals = x_vals - 2

# Plot line
plt.plot(x_vals, y_vals, 'k-')

# Inline label for the line
plt.text(9, 6, r'$y = x - 2$', fontsize=15, color='black')

# Plot points A and B
plt.scatter(*A, color='red', s=80)
plt.scatter(*B, color='blue', s=80)

# Annotate points near them
plt.text(A[0] + 0.3, A[1], r'A (7,1)', fontsize=12, color='red')
plt.text(B[0] + 0.3, B[1], r'B (3,5)', fontsize=12, color='blue')

# Axes settings
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Collection of points equidistant from A and B')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axis('equal')

# Display
plt.show()
