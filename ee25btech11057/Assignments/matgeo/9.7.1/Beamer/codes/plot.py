import numpy as np
import matplotlib.pyplot as plt

# Parameter 'a'
a = 2  # You can change this value

# Circle: x^2 + y^2 = 16a^2 → y = ±√(16a^2 - x^2)
x_circle = np.linspace(-4 * a, 4 * a, 800)
y_circle_upper = np.sqrt(16 * a**2 - x_circle**2)
y_circle_lower = -y_circle_upper

# Parabola: y^2 = 6ax → y = ±√(6ax)
x_parabola = np.linspace(0, 4 * a, 500)
y_parabola_upper = np.sqrt(6 * a * x_parabola)
y_parabola_lower = -y_parabola_upper

# Intersection points (analytical)
x_intersect = 2 * a
y_intersect = 2 * np.sqrt(3) * a

# Create plot
plt.figure(figsize=(8, 8))

# Shaded region between curves (upper and lower parts)
x_fill1 = np.linspace(0, x_intersect, 300)
x_fill2 = np.linspace(x_intersect, 4 * a, 300)
y_fill1_upper = np.sqrt(6 * a * x_fill1)
y_fill2_upper = np.sqrt(16 * a**2 - x_fill2**2)

plt.fill_between(x_fill1, y_fill1_upper, color='orange', alpha=0.4)
plt.fill_between(x_fill2, y_fill2_upper, color='orange', alpha=0.4)
plt.fill_between(x_fill1, -y_fill1_upper, color='orange', alpha=0.4)
plt.fill_between(x_fill2, -y_fill2_upper, color='orange', alpha=0.4)

# Plot circle
plt.plot(x_circle, y_circle_upper, 'b', linewidth=1.8)
plt.plot(x_circle, y_circle_lower, 'b', linewidth=1.8)

# Plot parabola
plt.plot(x_parabola, y_parabola_upper, 'g', linewidth=1.8)
plt.plot(x_parabola, y_parabola_lower, 'g', linewidth=1.8)

# Mark intersection points
plt.scatter([x_intersect, x_intersect], [y_intersect, -y_intersect], color='red', zorder=5)
plt.text(x_intersect + 0.3 * a, y_intersect, f"({x_intersect/a:.1f}a, {y_intersect/a:.2f}a)",
         color='red', fontsize=10)

# --- Label the curves near them directly ---
plt.text(-2.5 * a, 3.2 * a, r'$x^2 + y^2 = 16a^2$', color='blue', fontsize=12, rotation=-25)
plt.text(0.5 * a, 0.7 * a, r'$y^2 = 6ax$', color='green', fontsize=12, rotation=35)

# Axes setup
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-4.5 * a, 5.0 * a)
plt.ylim(-4.5 * a, 5.0 * a)

# Title and labels
plt.title(r"Region bounded by $x^2 + y^2 = 16a^2$ and $y^2 = 6ax$")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(alpha=0.3)
plt.savefig("../figs/fig16.png")
# Show plot
plt.show()

