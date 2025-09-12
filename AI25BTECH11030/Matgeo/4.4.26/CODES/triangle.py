import matplotlib.pyplot as plt
import numpy as np

# Vertices of the triangle
A = np.array([2, 5])
B = np.array([-4, 9])
C = np.array([-2, -1])

# Calculate midpoint M of BC
M = (B + C) / 2

# Plot triangle
plt.figure(figsize=(6,6))
triangle_points = np.array([A, B, C, A])
plt.plot(triangle_points[:,0], triangle_points[:,1], 'k-', label='Triangle ABC')

# Plot vertices
plt.plot(A[0], A[1], 'ro')
plt.plot(B[0], B[1], 'ro')
plt.plot(C[0], C[1], 'ro')

# Label vertices
plt.text(A[0]+0.2, A[1], 'A(2,5)', fontsize=12, color='red')
plt.text(B[0]+0.2, B[1], 'B(-4,9)', fontsize=12, color='red')
plt.text(C[0]+0.2, C[1], 'C(-2,-1)', fontsize=12, color='red')

# Plot median from A to midpoint M
plt.plot([A[0], M[0]], [A[1], M[1]], 'b--', linewidth=2, label='Median AM')

# Label midpoint M
plt.plot(M[0], M[1], 'go')
plt.text(M[0]+0.2, M[1], f'M({M[0]:.1f},{M[1]:.1f})', fontsize=12, color='green')

# Position to place equation on the median line midpoint
mid_x = (A[0] + M[0]) / 2
mid_y = (A[1] + M[1]) / 2

# Settings
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title('Triangle ABC with Median from A')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(-6, 4)
plt.ylim(-3, 11)

# Save the figure as PNG
filename = 'triangle_median_eqonline.png'
plt.savefig(filename)
plt.close()
