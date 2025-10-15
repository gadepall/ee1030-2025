# main_plot.py
# Code to plot the solution of the system of rational equations

import numpy as np
import matplotlib.pyplot as plt
# Although conics.py was provided, for direct plotting of implicit equations,
# it's more straightforward to use matplotlib's contour function.
# The parameters V, u, and f are used to define the equations below.

# --- Define the parameters for the two hyperbolas ---

# Hyperbola 1: 4(x^2 - y^2) - 12x + 8y = 0
V1 = np.array([[4, 0], [0, -4]])
u1 = np.array([-6, 4])
f1 = 0

# Hyperbola 2: -2(x^2 - y^2) - 10x + 20y = 0
V2 = np.array([[-2, 0], [0, 2]])
u2 = np.array([-5, 10])
f2 = 0

# --- Set up the plotting grid ---
# Generate a grid of points to evaluate the equations on
x_vals = np.linspace(-10, 15, 500)
y_vals = np.linspace(-10, 15, 500)
X, Y = np.meshgrid(x_vals, y_vals)

# --- Define the hyperbola equations ---
# Equation is x^T V x + 2u^T x + f = 0
# For a point (x,y), the vector is [x, y]
# So x^T V x becomes V[0,0]*x^2 + V[1,1]*y^2
# and 2u^T x becomes 2*(u[0]*x + u[1]*y)

eq1 = V1[0,0]*X**2 + V1[1,1]*Y**2 + 2*(u1[0]*X + u1[1]*Y) + f1
eq2 = V2[0,0]*X**2 + V2[1,1]*Y**2 + 2*(u2[0]*X + u2[1]*Y) + f2

# --- Create the Plot ---
plt.figure(figsize=(10, 10))

# Plot the hyperbolas by finding where their equations equal zero
plt.contour(X, Y, eq1, levels=[0], colors='red', linewidths=2)
plt.contour(X, Y, eq2, levels=[0], colors='blue', linewidths=2)

# --- Plot the Common Chord and Solution ---
# The common chord is 64x - 96y = 0, which simplifies to 2x - 3y = 0
# So, y = (2/3)x
plt.plot(x_vals, (2/3)*x_vals, 'g--', label='Common Chord: $2x - 3y = 0$')

# The solution point
solution_point = np.array([3, 2])
plt.plot(solution_point[0], solution_point[1], 'ko', markersize=10, label='Solution (3, 2)')

# --- Formatting ---
plt.title('Intersection of Hyperbolas', fontsize=16)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-5, 10)
plt.ylim(-5, 10)

# Create a legend
plt.legend(handles=[
    plt.Line2D([0], [0], color='red', lw=2, label='Hyperbola 1'),
    plt.Line2D([0], [0], color='blue', lw=2, label='Hyperbola 2'),
    plt.Line2D([0], [0], color='g', linestyle='--', label='Common Chord'),
    plt.Line2D([0], [0], marker='o', color='k', linestyle='', markersize=8, label='Solution (3, 2)')
])

# Save and show the plot
plt.savefig('hyperbola_intersection.png')
plt.show()
