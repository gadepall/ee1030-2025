import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x + 1

# Range for the curve
x_vals = np.linspace(1.5, 3.5, 200)
y_vals = f(x_vals)

# Intersection points
points = {
    "A": (2, f(2)),   # (2,3)
    "B": (3, f(3)),   # (3,4)
    "C": (3, 0),      # (3,0)
    "D": (2, 0)       # (2,0)
}

# Plot the line y = x+1
plt.plot(x_vals, y_vals, label=r"$y=x+1$", color="blue")

# Plot vertical lines x=2 and x=3
plt.axvline(2, color="black", linestyle="--", label=r"$x=2$")
plt.axvline(3, color="black", linestyle="--", label=r"$x=3$")

# Plot x-axis
plt.axhline(0, color="black")

# Shade the region (quadrilateral A-B-C-D)
x_poly = [points["A"][0], points["B"][0], points["C"][0], points["D"][0]]
y_poly = [points["A"][1], points["B"][1], points["C"][1], points["D"][1]]
plt.fill(x_poly, y_poly, color="skyblue", alpha=0.5, label="Shaded Region")

# Mark the intersection points
for name, (x, y) in points.items():
    plt.scatter(x, y, color="red")
    plt.text(x+0.05, y+0.1, f"{name}({x},{y})")

# Labels and legend
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Region bounded by y=x+1, x=2, x=3 and x-axis")
plt.legend()
plt.grid(True)
plt.axis("equal")

# Save the figure
plt.savefig("fig_8.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()
