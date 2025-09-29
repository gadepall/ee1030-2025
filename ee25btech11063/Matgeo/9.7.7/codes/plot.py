import numpy as np
import matplotlib.pyplot as plt

# Solution point from algebra
x_sol = 1
y_sol = -2

# Define ranges, avoiding x=0 and y=0
x_vals = np.linspace(0.1, 5, 400)
y_vals = np.linspace(-10, -0.1, 400)

# Create meshgrid
X, Y = np.meshgrid(x_vals, y_vals)

# Define the equations:
# 1. (3/x + 8/y + 1 = 0)
# 2. (1/x - 2/y - 2 = 0)
eq1 = (3 / X) + (8 / Y) + 1
eq2 = (1 / X) - (2 / Y) - 2

# Plot
plt.figure(figsize=(10, 6))

# Contour where each equation is zero
plt.contour(X, Y, eq1, levels=[0], colors='blue', linewidths=2, linestyles='solid')
plt.contour(X, Y, eq2, levels=[0], colors='green', linewidths=2, linestyles='solid')

# Plot point of intersection
plt.plot(x_sol, y_sol, 'ro', markersize=8, label=f'Solution (x={x_sol}, y={y_sol})')

# Labels and styling
plt.title('Plot of Two Nonlinear Equations with Solution Point')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True)
plt.legend()

# Save the plot
plt.savefig("equation_plot.png", dpi=300, bbox_inches='tight')
plt.close()  # Close the figure to avoid showing it if not needed

print("Plot saved as 'equation_plot.png'")

