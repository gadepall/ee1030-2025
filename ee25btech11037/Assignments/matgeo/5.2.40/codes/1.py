import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Load the C library and define the function signature ---

# Load the shared library named 'mat.so'
solver_lib = ctypes.CDLL('./mat.so')

# Define the argument types for the C function
solver_lib.solve_system.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
# Define the return type for the C function (int)
solver_lib.solve_system.restype = ctypes.c_int

# --- 2. Call the C function to solve the equations ---

# Define coefficients from the problem
a1, b1, c1 = 4.0, 3.0, 14.0
a2, b2, c2 = 3.0, -4.0, 23.0

# Create C-compatible double variables to store the results
x_sol = ctypes.c_double()
y_sol = ctypes.c_double()

# Call the C function
success = solver_lib.solve_system(
    a1, b1, c1, a2, b2, c2,
    ctypes.byref(x_sol), ctypes.byref(y_sol)
)

# --- 3. Process the result and plot ---

if success:
    # Get the Python values from the C types
    x_point = x_sol.value
    y_point = y_sol.value

    # Prepare data for plotting
    x_vals = np.linspace(-2, 2, 800)
    x_vals[x_vals == 0] = 1e-9 # Avoid division by zero

    # Rearrange equations to solve for y
    y1_vals = (c1 - a1 / x_vals) / b1
    y2_vals = (c2 - a2 / x_vals) / b2

    # Create the plot
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot the two functions
    ax.plot(x_vals, y1_vals, label=f'${int(a1)}/x + {int(b1)}y = {int(c1)}$')
    ax.plot(x_vals, y2_vals, label=f'${int(a2)}/x {int(b2)}y = {int(c2)}$')

    # Plot the intersection point
    ax.plot(x_point, y_point, 'ro', markersize=10, label='Intersection Point P')
    
    # Format and add the coordinate text
    coord_text = f'P ({x_point:.2f}, {y_point:.2f})'
    ax.text(x_point + 0.05, y_point, coord_text, fontsize=12, color='red', va='center')

    # Formatting
    ax.set_title('Solving System of Equations with Python and C', fontsize=16)
    ax.set_xlabel('x-axis', fontsize=12)
    ax.set_ylabel('y-axis', fontsize=12)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_ylim(-10, 10)
    ax.set_xlim(-2, 2)
    ax.legend(fontsize=12)
    ax.grid(True)

    # Save the figure
    plt.savefig('1.png')

    # Display the plot
    plt.show()
