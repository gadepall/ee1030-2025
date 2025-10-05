import numpy as np
import matplotlib.pyplot as plt
from call import solve_system

# Parameters
a, b, c = 2, 1, 5

# Solve for intersection
x_int, y_int = solve_system(a, b, c)

# Generate x values for plotting
x_vals = np.linspace(-5, 5, 200)

# Calculate y-values for each line
# Line 1: ax + by = c => y = (c - a*x) / b
y_line1 = (c - a * x_vals) / b

# Line 2: bx + ay = 1 + c => y = (1 + c - b*x) / a
y_line2 = (1 + c - b * x_vals) / a

# Plot lines
plt.plot(x_vals, y_line1, label=r'$ax + by = c$')
plt.plot(x_vals, y_line2, label=r'$bx + ay = 1 + c$')

# Plot intersection point
plt.scatter([x_int], [y_int], color='red', marker='X', s=100, label='Intersection Point')

plt.xlabel('x')
plt.ylabel('y')
plt.title('example graph for ax + by = c, bx + ay = 1 + c')
plt.grid(True)
plt.legend()
plt.show()

 
