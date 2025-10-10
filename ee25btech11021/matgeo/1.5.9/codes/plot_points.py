import numpy as np
import matplotlib.pyplot as plt

# Load points from .dat file
points = np.loadtxt("points.dat")

# Separate into X and Y coordinates
x = points[:, 0]
y = points[:, 1]

# Plot line along points A -> P -> B
plt.plot(x, y, 'b--', label="Line through A, P, B")

# Mark the points
plt.scatter(x[0], y[0], color='red', label="A(5, -6)")
plt.scatter(x[1], y[1], color='green', label="B(-1, -4)")
plt.scatter(x[2], y[2], color='purple', label="P(0, -13/3)")

# Labels and styling
plt.axvline(x=0, color='gray', linestyle=':')  # Y-axis
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Points and Line Division (Ratio 5:1)")
plt.legend()
plt.grid(True)

# ✅ Save the figure as PNG (you can change to .jpg or .pdf)
plt.savefig("points_plot.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()

