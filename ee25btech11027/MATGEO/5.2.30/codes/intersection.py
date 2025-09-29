import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Solve the system using the C library ---

# Load the shared library
    # Assumes the compiled library is in the same directory
c_lib = ctypes.CDLL('./intersection.so')


# Define the function signature to match the C function
solve_system_c = c_lib.solve_system
solve_system_c.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, 
                           ctypes.c_double, ctypes.c_double, ctypes.c_double,
                           ctypes.POINTER(ctypes.c_double), 
                           ctypes.POINTER(ctypes.c_double)]
solve_system_c.restype = None

# Create C-compatible double variables to store the results
x_sol = ctypes.c_double()
y_sol = ctypes.c_double()

# Call the C function with the coefficients
solve_system_c(7.0, -15.0, 2.0, 1.0, 2.0, 3.0, ctypes.byref(x_sol), ctypes.byref(y_sol))

# Get the Python values from the C types
x_intersect = x_sol.value
y_intersect = y_sol.value

print(f"Solution from C via Python: x = {x_intersect}, y = {y_intersect}")

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
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/5.2.30/figs/figure1.png")
plt.show()
