import matplotlib.pyplot as plt

# Define points of rectangle
points = [
    [0, 0],   # A
    [4, 0],   # B
    [4, -3],  # C
    [0, -3],  # D
    [0, 0]    # Closing rectangle back to A
]

# Labels for rectangle vertices
labels = ["(0,0)", "(4,0)", "(4,-3)", "(0,-3)"]

# Extract x and y coordinates
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

# Plot rectangle
plt.plot(x_vals, y_vals, "g--", label="Rectangle")

# Plot diagonal AC (from (0,0) to (4,-3))
plt.plot([0, 4], [0, -3], "b-", label="Diagonal")

# Mark points with red dots
plt.scatter([0, 4, 4, 0], [0, 0, -3, -3], color="red", label="Points")

# Add labels to each point
for (x, y), label in zip(points[:-1], labels):
    plt.text(x, y, label, fontsize=10, ha="center", va="bottom")

# Labels and grid
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Legend
plt.legend()

# Save figure
plt.savefig("fig2.png", dpi=300)

# Show plot
plt.show()

