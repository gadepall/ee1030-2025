import matplotlib.pyplot as plt

# Given points
A = (-2, 3)
B = (6, 7)
C = (8, 3)
D = (0, -1)  # calculated fourth vertex

# Plotting the parallelogram
x_coords = [A[0], B[0], C[0], D[0], A[0]]
y_coords = [A[1], B[1], C[1], D[1], A[1]]

plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'b-o')

# Plot diagonals
plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', label='Diagonal AC')
plt.plot([B[0], D[0]], [B[1], D[1]], 'g--', label='Diagonal BD')

# Label points
plt.text(A[0]-0.4, A[1]-0.3, 'A(-2,3)', fontsize=10)
plt.text(B[0]+0.1, B[1], 'B(6,7)', fontsize=10)
plt.text(C[0]+0.1, C[1]-0.3, 'C(8,3)', fontsize=10)
plt.text(D[0]-0.6, D[1]-0.3, 'D(0,-1)', fontsize=10)

# Axes and grid
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)

# Title and legend
plt.legend()
plt.title("Parallelogram ABCD with diagonals AC and BD")

# Save and show
plt.savefig("fig1.png", dpi=300, bbox_inches="tight")
plt.show()
