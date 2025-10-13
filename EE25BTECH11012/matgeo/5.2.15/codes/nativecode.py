import numpy as np
import matplotlib.pyplot as plt

# Create a range of x-values for plotting
x = np.linspace(-2, 6, 400)

# Rearrange the equations to solve for y
# Equation 1: 2x + y = 5  =>  y = 5 - 2x
y1 = 5 - 2 * x

# Equation 2: 3x + 2y = 8  =>  2y = 8 - 3x  =>  y = (8 - 3x) / 2
y2 = (8 - 3 * x) / 2

# --- Create the Plot ---
plt.figure(figsize=(10, 8))

# Plot the two lines
plt.plot(x, y1, label=r'$2x + y = 5$')
plt.plot(x, y2, label=r'$3x + 2y = 8$')

# The solution is the intersection point (2, 1)
solution_x = 2
solution_y = 1

# Plot and annotate the intersection point
plt.plot(solution_x, solution_y, 'ro', markersize=8, label=f'Solution ({solution_x}, {solution_y})')
plt.annotate(f'({solution_x}, {solution_y})', 
             xy=(solution_x, solution_y), 
             xytext=(solution_x + 0.2, solution_y + 0.2))

# --- Formatting the Graph ---
plt.title('Solution of the System of Equations', fontsize=16)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)
plt.show()