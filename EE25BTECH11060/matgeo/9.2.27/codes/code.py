import numpy as np
import matplotlib.pyplot as plt

# Define the x range
x = np.linspace(-5, 5, 500)

# Define the curves
y_curve = (3/4) * x**2      # 4y = 3x^2  => y = 3/4 x^2
y_line  = (3/2) * x + 6     # 2y = 3x+12 => y = 3/2 x + 6

# Plot the curves
plt.plot(x, y_curve, label=r'$4y=3x^2$', color='blue')
plt.plot(x, y_line, label=r'$2y=3x+12$', color='red')

# Find intersection points for shading
# Solve (3/4)x^2 = (3/2)x + 6  => 3x^2/4 - 3x/2 - 6 = 0
# Multiply by 4: 3x^2 - 6x - 24 = 0  => x^2 - 2x - 8 = 0
# Using quadratic formula: x = 1 ± 3
x1 = -2
x2 = 4

# Shade the area between the curves
x_fill = np.linspace(x1, x2, 500)
plt.fill_between(x_fill, (3/4)*x_fill**2, (3/2)*x_fill + 6, color='green', alpha=0.3, label='Shaded Area')

# Add labels, grid, and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Area between $4y=3x^2$ and $2y=3x+12$')
plt.grid(True)
plt.legend()
plt.show()
