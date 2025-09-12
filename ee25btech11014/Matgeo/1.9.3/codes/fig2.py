import matplotlib.pyplot as plt

# Define points of rectangle
points = [
    [0, 0],   # A
    [4, 0],   # B
    [4, -3],  # C
    [0, -3],  # D
    [0, 0]    # back to A to close
]

# Extract X and Y coordinates
x, y = zip(*points)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the rectangle edges
plt.plot(x, y, 'g--', label='Rectangle')

# Plot the diagonal line segment (A=(0,0) to C=(4,-3))
plt.plot([0, 4], [0, -3], 'b', linewidth=2, label='Diagonal')

# Mark the key points
plt.scatter(x, y, c='r', s=60, label='Points')

# Add labels
labels = ["(0,0)", "(4,0)", "(4,-3)", "(0,-3)", "(0,0)"]
for i, txt in enumerate(labels):
    plt.text(x[i]+0.1, y[i]+0.1, txt)

# Set labels and grid
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()
plt.axis('equal')  # keep rectangle proportions equal

# Save and show
plt.savefig('fig2.png', dpi=300)
plt.show()

