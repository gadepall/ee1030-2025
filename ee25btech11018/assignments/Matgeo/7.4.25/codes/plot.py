import sys
sys.path.insert(0, './')
import numpy as np
import matplotlib.pyplot as plt
from call import find_locus_equation

# Get the locus equation
locus_equation = find_locus_equation()
print(f"Locus equation: {locus_equation}")
fig, ax = plt.subplots(figsize=(9, 9))

# Given circle: x² + y² - 6x - 6y + 14 = 0
given_center = (3, 3)
given_radius = 2
given_circle = plt.Circle(given_center, given_radius, color='blue', fill=False, linewidth=2)
ax.add_patch(given_circle)

# Mark centre of given circle
ax.plot(*given_center, 'bo')
ax.text(given_center[0] + 0.2, given_center[1] + 0.2, "C₁(3,3)", color='blue', fontsize=11, fontweight='bold')

# Locus (Parabola):
x_vals = np.linspace(0.5, 9, 400)
sqrt_term = np.sqrt(np.maximum(0, 5 * (2 * x_vals - 1)))
y_plus = 3 + sqrt_term
y_minus = 3 - sqrt_term
ax.plot(x_vals, y_plus, 'r:', linewidth=2.5)
ax.plot(x_vals, y_minus, 'r:', linewidth=2.5)

# Write the parabola equation neatly near the curve
ax.text(6.7, 8.5, r"$y^2 - 10x - 6y + 14 = 0$", color='red', fontsize=13, fontweight='bold')

# Moving circle 
x_sample = 4
y_sample = 3 - np.sqrt(5 * (2 * x_sample - 1))
r_sample = x_sample  # because circle touches y-axis → r = x
moving_circle = plt.Circle((x_sample, y_sample), r_sample, color='green', fill=False, linewidth=2)
ax.add_patch(moving_circle)

# Mark the moving circle centre
ax.plot(x_sample, y_sample, 'go')
ax.text(x_sample + 0.3, y_sample - 0.4, "C(x,y)", color='green', fontsize=11, fontweight='bold')

# Formatting , Axes setup
ax.axvline(0, color='black', linestyle='-', linewidth=1.5)
ax.axhline(0, color='black', linestyle='-', linewidth=1.5)
ax.text(9.3, 0.2, "X-axis", fontsize=12, fontweight='bold')
ax.text(0.2, 9.4, "Y-axis", fontsize=12, fontweight='bold')
ax.set_xlim(-2, 10)
ax.set_ylim(-4, 11)
ax.set_aspect('equal', 'box')
ax.set_xlabel("x", fontsize=13)
ax.set_ylabel("y", fontsize=13)
ax.set_title("Locus of Centres of Circles Touching Given Circle and Y-axis", fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.6)

# Save and show
plt.tight_layout()
plt.savefig('fig.png', dpi=200, bbox_inches='tight')
plt.show()

