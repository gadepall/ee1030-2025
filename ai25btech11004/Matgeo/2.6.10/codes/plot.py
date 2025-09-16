import matplotlib.pyplot as plt

# Coordinates of the vertices
x = [-8, -6, -3]
y = [4, 6, 9]

# Plot points
plt.scatter(x, y, color='red', label='Vertices')

# Connect the points (straight line since collinear)
plt.plot(x, y, color='blue', linestyle='--', label='Line through points')

# Annotate the points
for i, txt in enumerate([f"({x[i]},{y[i]})" for i in range(len(x))]):
    plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(5,5))

# Labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Vertices of the Triangle (Actually Collinear)")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("triangle.png", dpi=300, bbox_inches="tight")

# Close the figure to free memory
plt.close()

print("Graph saved as triangle.png")

