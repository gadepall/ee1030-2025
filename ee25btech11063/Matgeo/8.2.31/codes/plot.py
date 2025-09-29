import numpy as np
import matplotlib.pyplot as plt

# Parameters of the ellipse
a = 3  # semi-major axis
b = 2  # semi-minor axis

# Generate theta values
theta = np.linspace(0, 2*np.pi, 400)

# Parametric equations of ellipse
x = a * np.cos(theta)
y = b * np.sin(theta)

# Plot ellipse
plt.plot(x, y, label=r"$\frac{x^2}{9}+\frac{y^2}{4}=1$")

# Mark ends of major axis (±3,0)
plt.scatter([3, -3], [0, 0], color="red", zorder=5, label="Major axis ends")

# Mark ends of minor axis (0,±2)
plt.scatter([0, 0], [2, -2], color="blue", zorder=5, label="Minor axis ends")

# Add annotations
plt.text(3.1, 0.1, "(3,0)", color="red")
plt.text(-3.7, 0.1, "(-3,0)", color="red")
plt.text(0.1, 2.1, "(0,2)", color="blue")
plt.text(0.1, -2.3, "(0,-2)", color="blue")

# Axes setup
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.gca().set_aspect('equal')  # keep aspect ratio equal
plt.legend()
plt.title("Ellipse with Major and Minor Axis Ends")
plt.grid(True)
plt.savefig("ellipse.png", dpi=300, bbox_inches="tight")
plt.show()

