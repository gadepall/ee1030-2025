import numpy as np
import matplotlib.pyplot as plt

# Load the file, using comma as delimiter
points = np.loadtxt("points.dat", delimiter=",")

# Take only the first two columns (x, y)
x = points[:, 0]
y = points[:, 1]

# --- Plot ---
plt.figure(figsize=(6, 6))
plt.scatter(x, y, color="red", s=60, label="Points")
plt.plot(x, y, linestyle="--", color="blue", label="Connection")

# Annotate each point
for xi, yi in zip(x, y):
    plt.text(xi + 0.1, yi + 0.1, f"({xi:g}, {yi:g})")

# Axes setup
ax = plt.gca()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot of Points from points.dat")
plt.grid(True, alpha=0.4)
plt.legend()

# Save the figure
plt.savefig("points_plot.png", dpi=300, bbox_inches="tight")

# Show the figure
plt.show()

