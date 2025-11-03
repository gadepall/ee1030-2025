import matplotlib.pyplot as plt

# Points
A = (2, 0)
B = (6, 1)
C1 = (2, 6)
C2 = (22/3, -14/3)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the points A, B, C1, and C2
ax.plot(A[0], A[1], 'bo', label="A(2, 0)", markersize=8)
ax.plot(B[0], B[1], 'go', label="B(6, 1)", markersize=8)
ax.plot(C1[0], C1[1], 'ro', label="C1(2, 6)", markersize=8)
ax.plot(C2[0], C2[1], 'mo', label="C2(22/3, -14/3)", markersize=8)

# Connect the points A, B, and C1 to form the first triangle
ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=2)  # AB
ax.plot([B[0], C1[0]], [B[1], C1[1]], 'k-', lw=2)  # BC1
ax.plot([C1[0], A[0]], [C1[1], A[1]], 'k-', lw=2)  # C1A

# Connect the points A, B, and C2 to form the second triangle
ax.plot([A[0], B[0]], [A[1], B[1]], 'k--', lw=2)  # AB
ax.plot([B[0], C2[0]], [B[1], C2[1]], 'k--', lw=2)  # BC2
ax.plot([C2[0], A[0]], [C2[1], A[1]], 'k--', lw=2)  # C2A

# Labels for the points
ax.text(A[0], A[1]-0.2, 'A(2, 0)', fontsize=12, ha='right', verticalalignment='top')
ax.text(B[0]+0.2, B[1], 'B(6, 1)', fontsize=12, ha='left', verticalalignment='top')
ax.text(C1[0]-0.3, C1[1], f'C1(2, 6)', fontsize=12, ha='right', verticalalignment='top')
ax.text(C2[0]-0.4, C2[1], f'C2({C2[0]:.2f}, {C2[1]:.2f})', fontsize=12, ha='right', verticalalignment='center')

# Set the axes limits
ax.set_xlim(-5, 10)
ax.set_ylim(-5, 10)

# Set labels and title
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Graph of the 2 Possible Triangles', fontsize=16)

# Show grid and customize
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)

# Show the legend
ax.legend(loc='upper left', fontsize=12)

# Show the plot
plt.show()
