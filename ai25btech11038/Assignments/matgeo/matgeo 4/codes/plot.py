import matplotlib.pyplot as plt

# Points
x = [-1, 0, 3]
y = [1, 5, 2]

# Plot points
plt.scatter(x, y, color="red", s=80)

# Connect points to form a triangle
plt.plot([x[0], x[1], x[2], x[0]], [y[0], y[1], y[2], y[0]], color="blue")

# Annotate points
labels = ["(-1,1)", "(0,5)", "(3,2)"]
for i in range(len(x)):
    plt.text(x[i] + 0.2, y[i] + 0.2, labels[i], fontsize=10)

# Axes
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.axis("equal")

plt.title("Triangle formed by three points")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
