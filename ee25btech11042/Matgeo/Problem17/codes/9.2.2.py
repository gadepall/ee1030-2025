import numpy as np
import matplotlib.pyplot as plt

# Let a = 1 for plotting
a = 1.0

# --- Define the parameters for the parabola and circle ---
# Parabola: y^2 - 6ax = 0
V1 = np.array([[0, 0], [0, 1]])
u1 = np.array([-3*a, 0])
f1 = 0

# Circle: x^2 + y^2 - 16a^2 = 0
V2 = np.array([[1, 0], [0, 1]])
u2 = np.array([0, 0])
f2 = -16*a**2

# --- Set up the plotting grid ---
x_vals = np.linspace(-8*a, 8*a, 800)
y_vals = np.linspace(-8*a, 8*a, 800)
X, Y = np.meshgrid(x_vals, y_vals)

# --- Define the conic equations ---
eq1 = Y**2 - 6*a*X
eq2 = X**2 + Y**2 - 16*a**2

# --- Create the Plot ---
plt.figure(figsize=(10, 10))

# Plot the curves
plt.contour(X, Y, eq1, levels=[0], colors='red', linewidths=2)
plt.contour(X, Y, eq2, levels=[0], colors='blue', linewidths=2)

# --- Shading the Region ---
x_intersect = 2 * a
# Part 1: Under the parabola from x=0 to x_intersect
x_fill_1 = np.linspace(0, x_intersect, 200)
y_fill_1_upper = np.sqrt(6 * a * x_fill_1)
plt.fill_between(x_fill_1, -y_fill_1_upper, y_fill_1_upper, color='gray', alpha=0.5)

# Part 2: Under the circle from x_intersect to x=4a
x_fill_2 = np.linspace(x_intersect, 4 * a, 200)
y_fill_2_upper = np.sqrt(16 * a**2 - x_fill_2**2)
plt.fill_between(x_fill_2, -y_fill_2_upper, y_fill_2_upper, color='gray', alpha=0.5)

# --- Plot the Solution Points ---
solution_point1 = np.array([2*a, 2*np.sqrt(3)*a])
solution_point2 = np.array([2*a, -2*np.sqrt(3)*a])
plt.plot(solution_point1[0], solution_point1[1], 'ko', markersize=8)
plt.plot(solution_point2[0], solution_point2[1], 'ko', markersize=8)

# --- Formatting ---
plt.title('Intersection of Parabola and Circle', fontsize=16)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-5*a, 5*a); plt.ylim(-5*a, 5*a)

# Create a legend
plt.legend(handles=[
    plt.Line2D([0], [0], color='red', lw=2, label='Parabola: $y^2=6ax$'),
    plt.Line2D([0], [0], color='blue', lw=2, label='Circle: $x^2+y^2=16a^2$'),
    plt.Line2D([0], [0], marker='o', color='k', linestyle='', markersize=8, label=f'Intersections at x={2*a:.1f}'),
    plt.Rectangle((0, 0), 1, 1, fc='gray', alpha=0.5, label='Shaded Region')
])

plt.savefig('direct_plot.png')
plt.show()
