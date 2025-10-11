import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, -3],
              [3,  2]])
b = np.array([7, 5])

# Solve the system Ax = b
solution = np.linalg.solve(A, b)
x_intersect, y_intersect = solution[0], solution[1]

# --- 2. Plot the graph ---

# Generate a range of x values for plotting the lines
x_vals = np.linspace(x_intersect - 10, x_intersect + 10, 400)

# Calculate y values for each equation
# Eq1: 2x - y = 10  => y = 2x - 10
y1_vals = (5 - 3 * x_vals) / 2
# Eq2: 3x + y = 5   => y = 5 - 3x
y2_vals =  (2 * x_vals - 7) / 3

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x_vals, y1_vals, color='blue')
plt.plot(x_vals, y2_vals, color='green')

# Mark and label the intersection point
plt.plot(x_intersect, y_intersect, 'ro', markersize=8)
plt.text(x_intersect + 1.0, y_intersect, f'({x_intersect:.2f}, {y_intersect:.2f})', fontsize=12)

# --- 3. Add non-overlapping labels directly to the lines ---

# Add text for the first equation '2x - y = 10'
# We choose an x-coordinate (e.g., 6) and calculate the corresponding y-coordinate on the line.
# A small offset is added to the y-coordinate to position the text slightly above the line.
plt.text(-5, 2.5, '3x + 2y = 5', color='blue', va='bottom', ha='center')

# Add text for the second equation '3x + y = 5'
# We choose a different x-coordinate (e.g., 1) to ensure the labels are spaced apart.
plt.text(12, 2.5, '2x - 3y = 7', color='green', va='bottom', ha='center')


# --- 4. Style the plot ---

plt.title('Solution of the System of Linear Equations')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axis('equal')
plt.show()