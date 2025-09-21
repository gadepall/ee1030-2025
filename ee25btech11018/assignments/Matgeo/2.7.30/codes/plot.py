import numpy as np
import matplotlib.pyplot as plt

# Given value of k
k = 3

# Coordinates of the points
A = np.array([k + 1, 1])
B = np.array([4, -3])
C = np.array([7, -k])

# Arrays for plotting
x_coords = [A[0], B[0], C[0], A[0]]  # Loop back to A
y_coords = [A[1], B[1], C[1], A[1]]

# Create figure
plt.figure(figsize=(7, 7))

# Shade the triangle region
plt.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='lightblue', alpha=0.5, label='Region ABC')

# Plot the triangle boundary
plt.plot(x_coords, y_coords, 'b-', linewidth=2, label='Triangle ABC')

# Plot points clearly
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color=['red', 'green', 'purple'], s=80, zorder=5)

# Annotate points slightly offset for clarity
plt.text(A[0] + 0.2, A[1] + 0.2, f"A({A[0]}, {A[1]})", fontsize=11, color='red', weight='bold')
plt.text(B[0] + 0.2, B[1] - 0.4, f"B({B[0]}, {B[1]})", fontsize=11, color='green', weight='bold')
plt.text(C[0] + 0.2, C[1] + 0.2, f"C({C[0]}, {C[1]})", fontsize=11, color='purple', weight='bold')

# Add grid and styling
plt.title("Triangle ABC with Shaded Area", fontsize=14, weight='bold')
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Set equal aspect ratio to avoid distortion
plt.axis('equal')

# Adjust limits so points are not too close to the axes
x_min, x_max = min(x_coords) - 1, max(x_coords) + 1
y_min, y_max = min(y_coords) - 1, max(y_coords) + 1
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# Show the plot
plt.show()

