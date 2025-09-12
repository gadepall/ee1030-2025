import matplotlib.pyplot as plt

# Vertices of the quadrilateral
points = [(-3, -1), (-2, -4), (4, -1), (3, 4)]
labels = ["A", "B", "C", "D"]

# Close the polygon by repeating the first point
x_vals = [p[0] for p in points] + [points[0][0]]
y_vals = [p[1] for p in points] + [points[0][1]]

# Shoelace formula for area
area = 0
for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % len(points)]
    area += x1*y2 - y1*x2
area = abs(area) / 2

# Plot quadrilateral
plt.figure(figsize=(7,7))
plt.plot(x_vals, y_vals, 'b-o', linewidth=2)

# Fill (shade) the quadrilateral
plt.fill(x_vals, y_vals, color="skyblue", alpha=0.5, label="Quadrilateral Area")

# Mark vertices with labels + coordinates
for (x, y), label in zip(points, labels):
    plt.text(x+0.2, y+0.2, f"{label}{(x,y)}", fontsize=11, color="red")

# Draw diagonal AC
A = points[0]  # (-3, -1)
C = points[2]  # (4, -1)
plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', linewidth=2, label="Diagonal AC")

# Formatting
plt.title(f"Quadrilateral ABCD (Area = {area} sq. units)")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()

# Save the figure
plt.savefig("fig_4.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()
