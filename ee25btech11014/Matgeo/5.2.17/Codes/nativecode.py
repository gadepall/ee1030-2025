import numpy as np
import matplotlib.pyplot as plt

# Define the two equations in terms of y
# x - 3y = 7  =>  y = (x - 7)/3
# 3x - 3y = 15  =>  y = x - 5
def line1(x):
    return (x - 7) / 3

def line2(x):
    return x - 5

# Solve intersection point (already known: x=4, y=-1)
intersection = (4, -1)

# Generate x values
x_vals = np.linspace(-2, 10, 100)

# Plot the lines
plt.plot(x_vals, line1(x_vals), label=r"$x - 3y = 7$", color="blue")
plt.plot(x_vals, line2(x_vals), label=r"$3x - 3y = 15$", color="green")

# Plot intersection point
plt.scatter(*intersection, color="red", zorder=5)
plt.text(intersection[0]+0.2, intersection[1]-0.5, f"({intersection[0]}, {intersection[1]})", color="red")

# Axis labels
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph of the system of equations")

# Grid, legend
plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save the figure
plt.savefig("LE.png", dpi=300, bbox_inches="tight")

# Show plot
plt.show()
