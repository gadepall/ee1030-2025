import matplotlib.pyplot as plt
import os

# Define square vertices (side length = 3)
points = [(0,0), (3,0), (3,3), (0,3), (0,0)]
labels = ["A", "B", "C", "D", "A"]  # A-B-C-D (close with A)

# Separate x and y coordinates
x, y = zip(*points)

plt.figure(figsize=(6,6))

# Plot square outline
plt.plot(x, y, color="black", linewidth=2)

# Fill square with light color
plt.fill(x, y, color="lightgrey", alpha=0.3)

# Draw vectors for each side with different colors
colors = ["red", "green", "blue", "purple"]
for i in range(4):
    x0, y0 = points[i]
    x1, y1 = points[i+1]
    dx, dy = x1 - x0, y1 - y0
    plt.quiver(x0, y0, dx, dy, angles="xy", scale_units="xy", scale=1,
               color=colors[i], width=0.005)

# Add vertex labels
for (xv, yv), label in zip(points[:-1], labels[:-1]):  # skip last duplicate point
    plt.text(xv - 0.2, yv - 0.2, label, fontsize=12, fontweight="bold", color="black")

# Formatting
plt.title("Square of Side 3 Units with Vectors and Vertices")
plt.axis("equal")
plt.grid(True)
plt.xlim(-1, 4)
plt.ylim(-1, 4)

# --- Save in ../figures folder ---
save_path = os.path.join("..", "figures", "square_plot.png")

# Create folder if it does not exist
os.makedirs(os.path.dirname(save_path), exist_ok=True)

plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.show()

