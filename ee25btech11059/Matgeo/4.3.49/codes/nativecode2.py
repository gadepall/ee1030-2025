import matplotlib.pyplot as plt
import numpy as np

# Define the line: y = (1/2)x - 2
x = np.linspace(-2, 8, 200)
y = 0.5 * x - 2

# Create plot
plt.figure(figsize=(6,6))
plt.plot(x, y, label=r"$y=\frac{1}{2}x-2$", color="blue")

# Mark intercepts
plt.scatter([4], [0], color="red", label="x-intercept (4,0)", zorder=5)
plt.scatter([0], [-2], color="green", label="y-intercept (0,-2)", zorder=5)

# Axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Labels
plt.xlabel("x")
plt.ylabel("y")
plt.title("Line: x - 2y = 4")
plt.legend()
plt.grid(True)

# Save and show
file_path = "line_plot.png"   # will save in current directory
plt.savefig(file_path)
plt.show()

print(f"Plot saved as {file_path}")
