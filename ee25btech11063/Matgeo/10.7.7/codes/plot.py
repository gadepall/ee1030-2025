import numpy as np
import matplotlib.pyplot as plt

# Define parabola 1: y^2 = 4x  -> x = y^2 / 4
y1 = np.linspace(-20, 20, 400)
x1 = (y1**2) / 4

# Define parabola 2: x^2 = -32y -> y = -x^2 / 32
x2 = np.linspace(-40, 40, 400)
y2 = -(x2**2) / 32

# Define common tangent: y = (1/2)x + 2
x_tan = np.linspace(-10, 50, 400)
y_tan = 0.5 * x_tan + 2

# Plot the parabolas
plt.figure(figsize=(8, 6))
plt.plot(x1, y1, 'b', label='y^2 = 4x')
plt.plot(x2, y2, 'g', label='x^2 = -32y')

# Plot the tangent line
plt.plot(x_tan, y_tan, 'r--', label='y = (1/2)x + 2')

# Add labels and title
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Common Tangent to Two Parabolas")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# Save as PNG file
plt.savefig("slope_plot.png", dpi=300)

# Show the plot
plt.show()

