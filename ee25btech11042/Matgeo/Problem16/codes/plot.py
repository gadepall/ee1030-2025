import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Load the C library and define the function signature ---

# Load the shared library (assumes 'liblinesolver.so' is in the same directory)
line_solver_lib = ctypes.CDLL('./liblinesolver.so')

# Get the function from the library
find_k = line_solver_lib.find_k_values

# Define the argument types (two pointers to double)
find_k.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
# Define the return type (void)
find_k.restype = None

# --- Call the C function ---

# Create C-compatible double variables to hold the results
k_pos = ctypes.c_double()
k_neg = ctypes.c_double()

# Call the C function, passing the variables by reference
find_k(ctypes.byref(k_pos), ctypes.byref(k_neg))

# Retrieve the Python float values from the ctypes objects
k1 = k_pos.value
k2 = k_neg.value

# --- Plotting the results ---

# Generate a range of x-values for the plot
x = np.linspace(-10, 10, 400)

# Original line: 5x - y + 1 = 0  =>  y = 5x + 1
y_orig = 5 * x + 1

# Solution Line 1 (L1): x + 5y = k1  =>  y = (-x + k1) / 5
y_L1 = (-x + k1) / 5

# Solution Line 2 (L2): x + 5y = k2  =>  y = (-x + k2) / 5
y_L2 = (-x + k2) / 5

# Set a plot style
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the lines
ax.plot(x, y_orig, 'r', label='Original Line: $5x - y + 1 = 0$')
ax.plot(x, y_L1, 'b', label=f'Line L1: $x + 5y = {k1:.2f}$')
ax.plot(x, y_L2, 'g', label=f'Line L2: $x + 5y = {k2:.2f}$')

# Fill the triangles to show the area
ax.fill([0, k1, 0], [0, 0, k1/5], 'blue', alpha=0.2, label='Area L1 = 5')
ax.fill([0, k2, 0], [0, 0, k2/5], 'green', alpha=0.2, label='Area L2 = 5')

# --- Formatting the plot ---
ax.set_title('Lines and Triangles Formed with Axes')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
# Draw coordinate axes
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
# Set plot limits and aspect ratio
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', adjustable='box')
ax.legend()

# Display the plot
plt.show()
