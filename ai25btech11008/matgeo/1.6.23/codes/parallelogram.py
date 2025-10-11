import matplotlib.pyplot as plt

# Define points
A = (3, 1)
B = (6, 4)
C = (8, 6)

# Plot points
points = [A, B, C]
labels = ['A(3,1)', 'B(6,4)', 'C(8,6)']
colors = ['blue', 'orange', 'green']

plt.figure(figsize=(6,6))
for (x,y), label, color in zip(points, labels, colors):
    plt.scatter(x, y, color=color, s=100, zorder=5)
    plt.text(x+0.1, y+0.1, label, fontsize=12, fontweight='bold')

# Draw line through all points (collinear check)
x_coords = [A[0], C[0]]
y_coords = [A[1], C[1]]
plt.plot(x_coords, y_coords, '--', color='gray', linewidth=2, label="Line through A, B, C")

# Axes and grid
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Title
plt.title("Collinearity Check: Points A(3,1), B(6,4), C(8,6)")

# Save figure
plt.savefig("fig1.png", dpi=150, bbox_inches="tight")

# Show
plt.show()

