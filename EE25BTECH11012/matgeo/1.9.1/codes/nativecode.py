import matplotlib.pyplot as plt
import numpy as np

# Define m and n
m = 3
n = 4

# Define the points A and B
A = np.array([m, -n])
B = np.array([-m, n])

# Calculate the distance between A and B
distance = 2 * np.sqrt(m**2 + n**2)
print(f"Distance between A{tuple(A)} and B{tuple(B)} is: {distance}")

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot points A and B
ax.scatter(A[0], A[1], color='red', s=100, label=f'A = {tuple(A)}')
ax.scatter(B[0], B[1], color='blue', s=100, label=f'B = {tuple(B)}')

# Draw line segment between A and B
ax.plot([A[0], B[0]], [A[1], B[1]], 'k--', alpha=0.6, label='Line Segment AB')

# Plot origin for reference
ax.scatter(0, 0, color='black', s=80, label='Origin (0,0)')

# Add labels for points
ax.text(A[0] + 0.2, A[1], 'A', fontsize=14)
ax.text(B[0] + 0.2, B[1], 'B', fontsize=14)
ax.text(0.2, 0.2, 'O', fontsize=14)

# Set plot limits with some margin
margin = max(abs(m), abs(n)) + 1
ax.set_xlim(-margin, margin)
ax.set_ylim(-margin, margin)

# Add grid, title, labels, legend
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title('Distance Between Points A and B', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.legend()

# Equal aspect ratio
ax.set_aspect('equal', adjustable='box')

plt.show()
