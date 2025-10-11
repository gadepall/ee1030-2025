import ctypes
import os
import platform
import sys
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Load the Pre-compiled C Library ---

# Determine the correct library file name based on the operating system
lib_file_name = "liblines.so"
if platform.system() == "Windows":
    lib_file_name = "liblines.dll"

# Check if the required library file exists before proceeding
if not os.path.exists(lib_file_name):
    print(f"Error: Shared library '{lib_file_name}' not found.", file=sys.stderr)
    print("Please compile 'lines.c' into a shared library first.", file=sys.stderr)
    print("\nOn Linux/macOS, use: gcc -shared -o liblines.so -fPIC lines.c", file=sys.stderr)
    print("On Windows, use:   gcc -shared -o liblines.dll lines.c", file=sys.stderr)
    sys.exit(1) # Stop the script if the library is missing

# Load the shared library
try:
    c_lib = ctypes.CDLL(os.path.abspath(lib_file_name))
except OSError as e:
    print(f"Error loading C library: {e}", file=sys.stderr)
    sys.exit(1)

# Define the C function's signature (argument types and return type)
# This tells Python how to correctly call the C function.
c_lib.calculate_rotated_lines.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
c_lib.calculate_rotated_lines.restype = None

# --- 2. Define Inputs and Call the C Function ---

# Define the inputs for the C function
# Original line: 1x - 2y = 3
a_orig, b_orig = 1.0, -2.0
# Point of intersection
x0, y0 = 3.0, 2.0
# Angle of rotation
angle_deg = 40.0

# Prepare C-compatible variables to store the output from the function
a1, b1, c1 = (ctypes.c_double(), ctypes.c_double(), ctypes.c_double())
a2, b2, c2 = (ctypes.c_double(), ctypes.c_double(), ctypes.c_double())

# Call the C function, passing pointers to the output variables
c_lib.calculate_rotated_lines(
    a_orig, b_orig, x0, y0, angle_deg,
    ctypes.byref(a1), ctypes.byref(b1), ctypes.byref(c1),
    ctypes.byref(a2), ctypes.byref(b2), ctypes.byref(c2)
)

# Print the results retrieved from the C function
print("--- Equations Calculated by C Function ---")
print(f"Line 1: ({a1.value:.4f})x + ({b1.value:.4f})y = {c1.value:.4f}")
print(f"Line 2: ({a2.value:.4f})x + ({b2.value:.4f})y = {c2.value:.4f}\n")


# --- 3. Generate Data for Plotting ---

# Create a range of x-values for the plot
x_vals = np.linspace(0, 6, 400)

# Calculate y-values for the original line: x - 2y = 3  =>  y = 0.5x - 1.5
y_original = 0.5 * x_vals - 1.5

# Calculate y-values for the new lines using the coefficients from the C function
# General form ax + by = c  =>  y = (-a/b)x + (c/b)
y_line1 = (-a1.value / b1.value) * x_vals + (c1.value / b1.value)
y_line2 = (-a2.value / b2.value) * x_vals + (c2.value / b2.value)


# --- 4. Create and Display the Plot ---

print("Displaying plot...")
# Set up the figure and axes
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the three lines with distinct colors and labels
ax.plot(x_vals, y_original, 'b-', label='Original Line: $x - 2y = 3$')
ax.plot(x_vals, y_line1, 'g-', label=f'Line 1 (+{angle_deg}° from C)')
ax.plot(x_vals, y_line2, 'm-', label=f'Line 2 (-{angle_deg}° from C)')

# Highlight the common intersection point
ax.plot(x0, y0, 'ro', markersize=10, label=f'Intersection Point ({x0}, {y0})')

# --- 5. Final Touches for Clarity ---

# Set the aspect ratio to 'equal' to ensure angles are displayed correctly
ax.set_aspect('equal', adjustable='box')

# Add titles, labels, and a legend
ax.set_title(f'Lines Through ({x0}, {y0}) Making a {angle_deg}° Angle (Calculated in C)', fontsize=16)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.legend(fontsize=11)
ax.grid(True)

# Show the plot
plt.show()

