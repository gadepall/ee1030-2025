import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors with the calculated lambda = 1 ---
lambda_val = 1
A = np.array([1, 1, 1])
B = np.array([2, 4, -5])
C = np.array([lambda_val, 2, 3])

# Calculate the resultant vectors ---
# Sum vector S = B + C
S = B + C
# Unit vector s_hat along S
s_hat = S / np.linalg.norm(S)

# Set up the 3D plot ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
origin = [0, 0, 0]

#  Plot all vectors from the origin ---
ax.quiver(*origin, *A, color='red', label=r'$\vec{A}$')
ax.quiver(*origin, *B, color='blue', label=r'$\vec{B}$')
ax.quiver(*origin, *C, color='green', label=r'$\vec{C}$ (with $\lambda=1$)')
ax.quiver(*origin, *S, color='purple', label=r'Sum Vector $\vec{S} = \vec{B} + \vec{C}$')
ax.quiver(*origin, *s_hat, color='orange', label=r'Unit Vector $\hat{s}$')

# Add text labels near the vector tips for clarity ---
ax.text(A[0], A[1], A[2], 'A', color='red', fontsize=12)
ax.text(B[0], B[1], B[2], 'B', color='blue', fontsize=12)
ax.text(C[0], C[1], C[2], 'C', color='green', fontsize=12)
ax.text(S[0], S[1], S[2], 'S', color='purple', fontsize=12)
ax.text(s_hat[0]*1.5, s_hat[1]*1.5, s_hat[2]*1.5, 'ŝ', color='orange', fontsize=14)

# Customize and display the plot ---
ax.set_title('Visualization of Vectors', fontsize=16)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
ax.set_zlim([-6, 6])
ax.legend()
ax.grid(True)
plt.show()
