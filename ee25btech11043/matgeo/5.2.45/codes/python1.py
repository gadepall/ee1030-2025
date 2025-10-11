import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library

lib_solver = ctypes.CDLL("./code10.so")


# Define the argument types and return type for the C function
lib_solver.solveLinearSystem.argtypes = [
    ctypes.c_double,  # a1
    ctypes.c_double,  # b1
    ctypes.c_double,  # c1
    ctypes.c_double,  # a2
    ctypes.c_double,  # b2
    ctypes.c_double,  # c2
    ctypes.POINTER(ctypes.c_double), # x_sol
    ctypes.POINTER(ctypes.c_double)  # y_sol
]
lib_solver.solveLinearSystem.restype = None

# Given system of linear equations:
# x + 2y = 2
# 2x + 3y = 3

# Coefficients for the first equation
a1_given, b1_given, c1_given = 1.0, 2.0, 2.0
# Coefficients for the second equation
a2_given, b2_given, c2_given = 2.0, 3.0, 3.0

# Create ctypes doubles to hold the results
x_solution = ctypes.c_double()
y_solution = ctypes.c_double()

# Call the C function to solve the system
lib_solver.solveLinearSystem(
    a1_given, b1_given, c1_given,
    a2_given, b2_given, c2_given,
    ctypes.byref(x_solution),
    ctypes.byref(y_solution)
)

x_found = x_solution.value
y_found = y_solution.value

print(f"The solution to the system is: x = {x_found:.2f}, y = {y_found:.2f}")

# Optional: Plotting the lines to visualize the intersection
# Define a range for x values
x_vals = np.linspace(-5, 5, 400)

# Calculate y values for the first equation: y = (2 - x) / 2
y1_vals = (c1_given - a1_given * x_vals) / b1_given

# Calculate y values for the second equation: y = (3 - 2x) / 3
y2_vals = (c2_given - a2_given * x_vals) / b2_given

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1_vals, label=f'{a1_given}x + {b1_given}y = {c1_given}')
plt.plot(x_vals, y2_vals, label=f'{a2_given}x + {b2_given}y = {c2_given}')

# Plot the intersection point
plt.scatter(x_found, y_found, color='red', s=100, zorder=5, label=f'Solution ({x_found:.2f}, {y_found:.2f})')
plt.annotate(f'({x_found:.2f},{y_found:.2f})', (x_found, y_found), textcoords="offset points", xytext=(5,5), ha='left', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of Linear Equations')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
