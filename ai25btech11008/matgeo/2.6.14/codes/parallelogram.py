import numpy as np
import matplotlib.pyplot as plt

# Define diagonals as numpy arrays
d1 = np.array([2, -1, 1])
d2 = np.array([1, 3, -1])

# Diagonal endpoints (parallelogram diagonals intersect at the origin)
A = -0.5 * d1
B = 0.5 * d1
C = -0.5 * d2
D = 0.5 * d2

# Parallelogram vertices: A+C, A+D, B+D, B+C
P1 = A + C
P2 = A + D
P3 = B + D
P4 = B + C

# Collect vertices for plotting closed shape
parallelogram = np.array([P1, P2, P3, P4, P1])

# 3D plot
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Plot parallelogram edges
ax.plot(parallelogram[:,0], parallelogram[:,1], parallelogram[:,2], 'b-', label="Parallelogram")

# Fill parallelogram face
ax.plot_trisurf(parallelogram[:,0], parallelogram[:,1], parallelogram[:,2], color='cyan', alpha=0.5)

# Plot diagonals
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'r--', label="d1")
ax.plot([C[0], D[0]], [C[1], D[1]], [C[2], D[2]], 'g--', label="d2")

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Parallelogram with diagonals d1 and d2')
ax.legend()

plt.show()
