import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# --- Problem: Income and Expenditure ---
# The ratio of incomes of two persons is 9:7 => Incomes: 9x, 7x
# The ratio of their expenditures is 4:3   => Expenditures: 4y, 3y
# Each saves 2000 per month.
#
# Equations:
# 1) Income1 - Expenditure1 = Savings  => 9x - 4y = 2000
# 2) Income2 - Expenditure2 = Savings  => 7x - 3y = 2000

# Represent the system as Ax = B
# A = [[9, -4],
#      [7, -3]]
# x = [x_multiplier, y_multiplier]
# B = [2000, 2000]

A_matrix = np.array([[9.0, -4.0],
                 [7.0, -3.0]])

B_vector = np.array([2000.0, 2000.0])

print("Solving the system of equations for income and expenditure multipliers:")
print(f"  Equation 1: {A_matrix[0,0]}x + {A_matrix[0,1]}y = {B_vector[0]}")
print(f"  Equation 2: {A_matrix[1,0]}x + {A_matrix[1,1]}y = {B_vector[1]}")

 # Solve the system of linear equations using numpy.linalg.solve
solution = LA.solve(A_matrix, B_vector)
x_solution = solution[0]
y_solution = solution[1]

print(f"\nSolution found (intersection point):")
print(f"  x (income multiplier) = {x_solution:.2f}")
print(f"  y (expenditure multiplier) = {y_solution:.2f}")

   # --- Plotting the two lines and their intersection ---
plt.figure(figsize=(10, 8))

# Define a generous range for x_vals for plotting purposes.
# Knowing the solution (x=2000, y=4000), we can set a reasonable range.
x_plot_min = x_solution - 1000
x_plot_max = x_solution + 1000
x_vals_range = np.linspace(x_plot_min, x_plot_max, 400)

# Plotting Equation 1: a1*x + b1*y = c1  => y = (c1 - a1*x) / b1
# Coefficients from A_matrix and B_vector
y1_vals = (B_vector[0] - A_matrix[0,0] * x_vals_range) / A_matrix[0,1]
plt.plot(x_vals_range, y1_vals, "b-", label=f'{A_matrix[0,0]:.0f}x {A_matrix[0,1]:+.0f}y = {B_vector[0]:.0f} (Person 1)')
# Plotting Equation 2: a2*x + b2*y = c2  => y = (c2 - a2*x) / b2
y2_vals = (B_vector[1] - A_matrix[1,0] * x_vals_range) / A_matrix[1,1]
plt.plot(x_vals_range, y2_vals, "r-", label=f'{A_matrix[1,0]:.0f}x {A_matrix[1,1]:+.0f}y = {B_vector[1]:.0f} (Person 2)')

 # Plot the intersection point
plt.scatter(x_solution, y_solution, color='green', s=150, zorder=5,
            label=f'Intersection ({x_solution:.0f}, {y_solution:.0f})')
plt.annotate(f'({x_solution:.0f}, {y_solution:.0f})',
             (x_solution, y_solution), textcoords="offset points", xytext=(5,5), ha='left',
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="b", lw=1, alpha=0.7))

plt.xlabel('Income Multiplier (x)')
plt.ylabel('Expenditure Multiplier (y)')
plt.title('Graphical Solution of Income and Expenditure Equations')
plt.grid(True)
plt.legend(loc='best') # Places the legend in the best position
    
# Set plot limits based on data for good visualization
y_plot_min = min(y1_vals.min(), y2_vals.min(), y_solution) - 500
y_plot_max = max(y1_vals.max(), y2_vals.max(), y_solution) + 500
plt.xlim(x_plot_min, x_plot_max)
plt.ylim(y_plot_min, y_plot_max)
    
plt.gca().set_aspect('auto', adjustable='box') # 'auto' for potentially different scales on axes
    
plt.savefig("fig2.png")
plt.show()

print("Figure saved as fig2.png")
