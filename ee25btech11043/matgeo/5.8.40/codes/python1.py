import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib_solver = ctypes.CDLL("./code12.so")


# Define the argument types and return type for the C function
# int solve_2x2_system(double a1, double b1, double c1,
#                      double a2, double b2, double c2,
#                      double *x_solution, double *y_solution)
lib_solver.solve_2x2_system.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # a1, b1, c1
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # a2, b2, c2
    ctypes.POINTER(ctypes.c_double),                     # x_solution
    ctypes.POINTER(ctypes.c_double)                      # y_solution
]
lib_solver.solve_2x2_system.restype = ctypes.c_int

# --- Problem: Income and Expenditure ---
# Equations:
# 1) 9x - 4y = 2000
# 2) 7x - 3y = 2000

# Coefficients for the C solver
a1, b1, c1 = 9.0, -4.0, 2000.0
a2, b2, c2 = 7.0, -3.0, 2000.0

# Create ctypes doubles to hold the results for x and y multipliers
x_multiplier_result = ctypes.c_double()
y_multiplier_result = ctypes.c_double()

# Call the C function to solve the system
print("Solving the system of equations for income and expenditure multipliers using C function:")
print(f"  Equation 1: {a1}x + {b1}y = {c1}")
print(f"  Equation 2: {a2}x + {b2}y = {c2}")

success = lib_solver.solve_2x2_system(
    a1, b1, c1,
    a2, b2, c2,
    ctypes.byref(x_multiplier_result),
    ctypes.byref(y_multiplier_result)
)

if success: # `success` will now be 1 (True) or 0 (False)
    x_solution = x_multiplier_result.value
    y_solution = y_multiplier_result.value

    print(f"\nSolution found (intersection point):")
    print(f"  x (income multiplier) = {x_solution:.2f}")
    print(f"  y (expenditure multiplier) = {y_solution:.2f}")

    # --- Plotting the two lines and their intersection ---
    plt.figure(figsize=(10, 8))

    # Generate points for the lines
    # We'll use a range around the solution to make the intersection clear
    x_vals_range = np.linspace(x_solution - 1000, x_solution + 1000, 400) # Extend range for visualization

    # Plotting Eq 1: a1*x + b1*y = c1  => y = (c1 - a1*x) / b1
    if b1 != 0:
        y1_vals = (c1 - a1 * x_vals_range) / b1
        plt.plot(x_vals_range, y1_vals, label=f'{a1:.0f}x + {b1:.0f}y = {c1:.0f} (Eq 1)', color='blue')
    elif a1 != 0: # Handle vertical line case: x = c1/a1
        plt.axvline(x=c1/a1, label=f'x = {c1/a1:.0f} (Eq 1)', color='blue', linestyle='--')
    else:
        print("Equation 1 is trivial (0=C). Not plotted.")

    # Plotting Eq 2: a2*x + b2*y = c2  => y = (c2 - a2*x) / b2
    if b2 != 0:
        y2_vals = (c2 - a2 * x_vals_range) / b2
        plt.plot(x_vals_range, y2_vals, label=f'{a2:.0f}x + {b2:.0f}y = {c2:.0f} (Eq 2)', color='red')
    elif a2 != 0: # Handle vertical line case: x = c2/a2
        plt.axvline(x=c2/a1, label=f'x = {c2/a2:.0f} (Eq 2)', color='red', linestyle='--')
    else:
        print("Equation 2 is trivial (0=C). Not plotted.")

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
    plt.legend()
    plt.gca().set_aspect('auto', adjustable='box')
    plt.xlim(min(x_vals_range), max(x_vals_range))
    plt.ylim(min(y1_vals.min(), y2_vals.min(), y_solution) - 500, max(y1_vals.max(), y2_vals.max(), y_solution) + 500)
    plt.show()

else:
    print("\nError: No unique solution exists for this system (determinant is zero).")
    print("The lines are either parallel or the same line, which should not happen for this problem.")
