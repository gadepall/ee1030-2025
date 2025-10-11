import numpy as np
import matplotlib.pyplot as plt

# Quadratic coefficients
a, b, c = 1, 3, -10   # y = x^2 + 3x - 10

# Compute discriminant
D = b**2 - 4*a*c

# Real roots
r1 = (-b + np.sqrt(D)) / (2*a)
r2 = (-b - np.sqrt(D)) / (2*a)

# Generate parabola
x_vals = np.linspace(min(r1, r2) - 2, max(r1, r2) + 2, 400)
y_vals = a * x_vals**2 + b * x_vals + c

plt.axhline(0, color="black", linewidth=0.8)  # x-axis
plt.axvline(0, color="black", linewidth=0.8)  # y-axis

# Plot parabola
plt.plot(x_vals, y_vals, label="$y = x^2 + 3x - 10$", color="blue")

# Mark and annotate roots
plt.scatter([r1, r2], [0, 0], color="red", zorder=5)
plt.text(r1, -1, f"A({r1:.0f}, 0)", fontsize=11, color="red", ha="center")
plt.text(r2, -1, f"B({r2:.0f}, 0)", fontsize=11, color="red", ha="center")

plt.title("Quadratic Curve and Roots")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig('2.png')
plt.show()

