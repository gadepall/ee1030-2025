import numpy as np
import matplotlib.pyplot as plt

# --- Line equations ---
# Line 1: x + 2y = 10
# Line 2: 2x + y = -5
# Line 3: 5x + 4y = 0

# Coefficients for Ax = b
A = np.array([[1, 2],
              [2, 1]], dtype=float)
b = np.array([10, -5], dtype=float)

# Solve for intersection
det_A = np.linalg.det(A)
if det_A == 0:
    print("Lines 1 and 2 are parallel, no intersection.")
    intersection_exists = False
    xi = yi = None
else:
    xi, yi = np.linalg.solve(A, b)
    intersection_exists = True
    print(f"Intersection point: ({xi:.2f}, {yi:.2f})")

# Check if line 3 passes through intersection
if intersection_exists:
    # Line 3: 5x + 4y = 0
    check = 5*xi + 4*yi
    if abs(check) < 1e-8:  # small tolerance for floating point
        print("The line 5x + 4y = 0 passes through the intersection point.")
    else:
        print("The line 5x + 4y = 0 does NOT pass through the intersection point.")

# --- Plot the lines ---
x_vals = np.linspace(-10, 10, 400)

# Line 1: x + 2y = 10 => y = (10 - x)/2
y1 = (10 - x_vals)/2

# Line 2: 2x + y = -5 => y = -5 - 2*x
y2 = -5 - 2*x_vals

# Line 3: 5x + 4y = 0 => y = -5/4 * x
y3 = -5/4 * x_vals

plt.figure(figsize=(8,6))
plt.plot(x_vals, y1, label=r'$(1\ 2)\mathbf{x} = 10$', color='blue')
plt.plot(x_vals, y2, label=r'$(2\ 1)\mathbf{x} = -5$', color='green')
plt.plot(x_vals, y3, label=r'$(5\ 4)\mathbf{x} = 0$', color='red')

# Mark the intersection point
if intersection_exists:
    plt.scatter(xi, yi, color='black', zorder=5)
    plt.text(xi+0.5, yi, f'({xi:.2f},{yi:.2f})', fontsize=10)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersection of Lines')
plt.grid(True)
plt.legend()
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Save figure
plt.savefig('fig8.png', dpi=300)
plt.show()
