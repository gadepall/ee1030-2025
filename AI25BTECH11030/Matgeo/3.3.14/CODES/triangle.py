import matplotlib.pyplot as plt
import numpy as np

# Define vertices A, B, C
A = np.array([0, 0])
B = np.array([6, 0])
C = np.array([6 * np.cos(np.radians(90)), 8 * np.sin(np.radians(90))])  # (0, 8)

# Create plot
plt.figure(figsize=(6,6))

# Draw triangle sides
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label='AB = 6 cm')
plt.plot([B[0], C[0]], [B[1], C[1]], 'g-', label='BC = 8 cm')
plt.plot([C[0], A[0]], [C[1], A[1]], 'r-', label='AC (hypotenuse)')

# Mark points with labels and coordinates
plt.plot(A[0], A[1], 'ko')
plt.text(A[0]-1, A[1]-0.5, 'A (0, 0)', fontsize=12, fontweight='bold')

plt.plot(B[0], B[1], 'ko')
plt.text(B[0]+0.2, B[1]-0.5, 'B (6, 0)', fontsize=12, fontweight='bold')

plt.plot(C[0], C[1], 'ko')
plt.text(C[0]-3, C[1]+0.2, 'C (6 cos 90°, 8 sin 90°)', fontsize=12, fontweight='bold')

# Set axes limits and grid
plt.xlim(-4, 8)
plt.ylim(-2, 10)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Title and legend
plt.title('Right Triangle ABC with sides 6 cm and 8 cm')
plt.legend()

# Save plot as PNG file
plt.savefig('triangle_abc_with_expr_coords.png')

# Close plot
plt.close()
