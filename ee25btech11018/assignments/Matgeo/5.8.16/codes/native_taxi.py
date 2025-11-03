import numpy as np
import matplotlib.pyplot as plt

# Define y = (const - x)/coefficient equations
x_vals = np.linspace(-20, 120, 400)

# Line equations
y1 = (105 - x_vals) / 10
y2 = (155 - x_vals) / 15
y3 = (255 - x_vals) / 25  # c = 255

# Intersection point (x=5, y=10)
x_int, y_int = 5, 10

# Plot all lines
plt.figure(figsize=(8,6))
plt.plot(x_vals, y1, label="x + 10y = 105", linewidth=2)
plt.plot(x_vals, y2, label="x + 15y = 155", linewidth=2)
plt.plot(x_vals, y3, label="x + 25y = 255", linewidth=2)

# Mark intersection
plt.scatter(x_int, y_int, color='red', s=80, zorder=5, label="Intersection (5, 10)")

# Annotate intersection
plt.text(x_int + 2, y_int, "(5, 10)", color='red', fontsize=10, fontweight='bold')

# Labels and title
plt.title("Graph of Taxi Fare Equations", fontsize=14, fontweight='bold')
plt.xlabel("x (Fixed Charge ₹)")
plt.ylabel("y (Charge per km ₹)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.axis("equal")  # to maintain aspect ratio
plt.tight_layout()
plt.show()

