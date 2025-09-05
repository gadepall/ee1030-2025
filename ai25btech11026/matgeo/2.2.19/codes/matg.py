import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vectors
v1 = np.array([2, 4, -5])
v2 = np.array([1, 2, 3])  # λi + 2j + 3k

# λ = 1 solution
lam = 1
v_sum = np.array([2+lam, 6, -2])

# Vector (i + j + k)
u = np.array([1, 1, 1])

# Create A4 figure (8.27 × 11.7 inches)
fig = plt.figure(figsize=(8.27, 11.7))
ax = fig.add_subplot(111, projection='3d')

# Plot vectors
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='2i+4j-5k')
ax.quiver(0, 0, 0, lam*v2[0], lam*v2[1], lam*v2[2], color='b', label='λi+2j+3k (λ=1)')
ax.quiver(0, 0, 0, v_sum[0], v_sum[1], v_sum[2], color='g', label='Sum vector')
ax.quiver(0, 0, 0, u[0], u[1], u[2], color='m', label='i+j+k')

# Labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Graph of Vectors (λ=1)', fontsize=14)
ax.legend()

# Save as A4 size PDF and PNG
plt.savefig("vector_solution_lambda_A4.png", dpi=300, bbox_inches='tight')
plt.savefig("vector_solution_lambda_A4.pdf", bbox_inches='tight')

plt.show()

print("Saved as vector_solution_lambda_A4.png and vector_solution_lambda_A4.pdf")t