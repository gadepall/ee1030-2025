import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Part 1: CTYPES SETUP TO CALL THE C FUNCTION ---

# Define the name of the shared library based on the OS
lib_name = "libsolver.so" if os.name != "nt" else "solver.dll"
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)

# Load the shared library
try:
    c_lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading C library: {e}")
    print("Please ensure you have compiled solver.c into a shared library.")
    exit()

# Define the function signature (argument types and return type)
# This must match the C function's signature exactly
solve_func = c_lib.solveLinearSystem
solve_func.restype = ctypes.c_int
solve_func.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double, # a1, b1, c1
    ctypes.c_double, ctypes.c_double, ctypes.c_double, # a2, b2, c2
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double) # *x, *y
]

# --- Part 2: SOLVE THE SYSTEM USING THE C FUNCTION ---

# Coefficients from the equations:
# 2x - 3y = 8
a1, b1, c1 = 2.0, -3.0, 8.0
# 4x - 6y = 9
a2, b2, c2 = 4.0, -6.0, 9.0

# Create C-compatible double variables to hold the solution
x_sol = ctypes.c_double()
y_sol = ctypes.c_double()

# Call the C function, passing the variables by reference
status = solve_func(a1, b1, c1, a2, b2, c2, ctypes.byref(x_sol), ctypes.byref(y_sol))

# Process the result from the C function
solution_text = ""
solution_point = None
if status == 1:
    solution_point = (x_sol.value, y_sol.value)
    solution_text = f"Unique Solution found by C function: x={solution_point[0]:.2f}, y={solution_point[1]:.2f}"
elif status == 0:
    solution_text = "No Solution"
elif status == -1:
    solution_text = "Infinite Solutions"

print(solution_text)

# Create a range of x values
x = np.linspace(-10, 10, 400)

# Rearrange the equations into slope-intercept form (y = mx + c)
# Equation 1: 2x - 3y = 8  =>  y = (2/3)x - 8/3
y1 = (2/3)*x - (8/3)

# Equation 2: 4x - 6y = 9  =>  y = (4/6)x - 9/6  =>  y = (2/3)x - 3/2
y2 = (2/3)*x - (3/2)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the lines
plt.plot(x, y1, label='2x - 3y = 8', color='blue')
plt.plot(x, y2, label='4x - 6y = 9', color='red')

# Add titles and labels for clarity
plt.title('Plot of Inconsistent System of Equations', fontsize=16)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)

# Add a grid and set axis limits
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Display a legend to identify the lines
plt.legend()

# Show the plot
plt.show()
