import numpy as np
import matplotlib.pyplot as plt

# Function to solve a 2x2 system of linear equations
def solve_2x2_system(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None, None # No unique solution
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return x, y 

# Given equations
# x + 2y = 2
# 2x + 3y = 3

a1, b1, c1 = 1, 2, 2
a2, b2, c2 = 2, 3, 3

# Solve the system
x_solution, y_solution = solve_2x2_system(a1, b1, c1, a2, b2, c2)

if x_solution is not None and y_solution is not None:
    print(f"Solution: x = {x_solution}, y = {y_solution}")

    # Generate points for plotting the lines
    x_vals = np.linspace(-5, 5, 400)

    # First equation: x + 2y = 2  => y = (2 - x) / 2
    y1_vals = (2 - x_vals) / 2

    # Second equation: 2x + 3y = 3 => y = (3 - 2x) / 3
    y2_vals = (3 - 2 * x_vals) / 3

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y1_vals, label='x + 2y = 2')
    plt.plot(x_vals, y2_vals, label='2x + 3y = 3')

    # Plot the intersection point
    plt.plot(x_solution, y_solution, 'ro', markersize=8, label=f'Solution: ({x_solution:.2f}, {y_solution:.2f})')
    plt.annotate(f'({x_solution:.2f}, {y_solution:.2f})', (x_solution, y_solution),
                 textcoords="offset points", xytext=(10,10), ha='center')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solution of a System of Linear Equations')
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.7)
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.7)
    plt.grid(True)
    plt.legend()
    plt.axis('equal') # Ensures equal scaling for x and y axes
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.savefig("fig2.png")
    plt.show()

    print("Figure saved as fig2.png")
else:
    print("The system has no unique solution (lines are parallel or coincident).")
