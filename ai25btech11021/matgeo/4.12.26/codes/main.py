import numpy as np
import matplotlib.pyplot as plt

# 1. Define the constant c and the locus equation (Locus: x^2 + y^2 = c^2)
c = 5.0
c_squared = c * c

# Generate points for the circle (Locus)
theta = np.linspace(0, 2 * np.pi, 100)
x_locus = c * np.cos(theta)
y_locus = c * np.sin(theta)

# 2. Define a specific variable line and its foot of the perpendicular P(x0, y0)
# We choose P(3, 4), which satisfies x0^2 + y0^2 = 25
x0 = 3.0
y0 = 4.0

# The line equation is x*x0 + y*y0 = x0^2 + y0^2.
# Intercepts: a = c^2/x0 and b = c^2/y0
a = 25.0 / x0
b = 25.0 / y0

# Generate points for the variable line L
# Equation of the line: y = (c^2 - x*x0) / y0
x_line = np.linspace(0, a, 100)
y_line = (c_squared - x_line * x0) / y0

# 3. Create the plot
plt.figure(figsize=(8, 8))

# Plot the Locus (Circle)
plt.plot(x_locus, y_locus, 'r--', label=f'Locus: $x^2 + y^2 = {c_squared:.0f}$')

# Plot the Variable Line L
plt.plot(x_line, y_line, 'b-', label=f'Variable Line L: $\\frac{{x}}{{{a:.2f}}} + \\frac{{y}}{{{b:.2f}}} = 1$')

# Plot the Foot of the Perpendicular P
plt.plot(x0, y0, 'go', markersize=8, label=f'Foot of Perpendicular P({x0:.0f}, {y0:.0f})')

# Plot the Perpendicular Segment OP
plt.plot([0, x0], [0, y0], 'g-', linestyle=':', linewidth=2, label='Perpendicular Segment $\\mathbf{OP}$')

# Plot the Origin O
plt.plot(0, 0, 'kx', markersize=8, label='Origin O(0, 0)')

# Set limits and aspect ratio
plt.xlim(-c - 2, c + 2)
plt.ylim(-c - 2, c + 2)
plt.gca().set_aspect('equal', adjustable='box')

# Add labels and title
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Locus of the Foot of the Perpendicular')
plt.grid(True)
plt.legend(loc='lower left')

# Save the plot
plt.savefig('locus_plot.png')
plt.close()