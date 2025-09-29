import numpy as np
import matplotlib.pyplot as plt

# --- 1. Solve the system using NumPy ---

# Define the coefficient matrix A and the constant vector b
# 7x - 15y = 2
# 1x +  2y = 3
A = np.array([[7, -15], 
              [1,  2]])
b = np.array([2, 3])

# Solve the system Ax = b for x
solution = np.linalg.solve(A, b)
x_intersect, y_intersect = solution[0], solution[1]

print(f"Solution from Native Python: x = {x_intersect}, y = {y_intersect}")

# --- 2. Plot the graph ---

# Generate a range of x values around the intersection point
x_vals = np.linspace(x_intersect - 2, x_intersect + 2, 400)

# Calculate y values for each equation
# Eq1: 7x - 15y = 2  => y = (7x - 2) / 15
y1_vals = (7 * x_vals - 2) / 15
# Eq2: x + 2y = 3   => y = (3 - x) / 2
y2_vals = (3 - x_vals) / 2

# Create the plot
plt.figure(figsize=(8, 7))
plt.plot(x_vals, y1_vals, label='7x - 15y = 2', color='blue')
plt.plot(x_vals, y2_vals, label='x + 2y = 3', color='green')

# Mark and label the intersection point
plt.plot(x_intersect, y_intersect, 'ro', markersize=8, label=f'Intersection ({x_intersect:.2f}, {y_intersect:.2f})')
plt.text(x_intersect + 0.1, y_intersect, f'({x_intersect:.2f}, {y_intersect:.2f})', fontsize=12)

# Style the plot
plt.title('Figure')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.axis('equal')
plt.show()
