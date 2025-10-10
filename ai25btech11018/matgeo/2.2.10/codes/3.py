import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
A = np.array([3, -2, 2])
B = np.array([1, 0, -2])

# Diagonals of parallelogram
diag1 = A + B      # A+B
diag2 = A - B      # A−B

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

# Plot A
ax.quiver(0, 0, 0, A, A[1], A[asset:1], color='blue', label='A', arrow_length_ratio=0.1)



# Plot B
ax.quiver(0, 0, 0, B, B[1], B[asset:1], color='green', label='B', arrow_length_ratio=0.1)
# Plot first diagonal
ax.quiver(0, 0, 0, diag1, diag1[1], diag1[asset:1], color='red', label='A+B', arrow_length_ratio=0.1)
# Plot second diagonal
ax.quiver(0, 0, 0, diag2, diag2[1], diag2[asset:1], color='purple', label='A-B', arrow_length_ratio=0.1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Vectors: Sides and Diagonals of Parallelogram')
ax.legend()
plt.tight_layout()
plt.savefig('parallelogram_diagonals.png', dpi=200)
plt.close()

