import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Load the C library and set up the function ---


c_lib = ctypes.CDLL('./code.so')

# Get the function from the library
find_p_prime_func = c_lib.find_p_prime

# Define the argument types for the C function:
# (double, double, double, double, pointer_to_double_array)
find_p_prime_func.argtypes = [ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.POINTER(ctypes.c_double)]

# The C function has a 'void' return type
find_p_prime_func.restype = None


# --- Step 2: Define inputs, call the C function, and get results ---

# Input data from the problem
p_coords = (10.0, 3.0)
center_coords = (6.0, 0.0)

# Create the data type for the output array (an array of 2 doubles)
DoubleArray2 = ctypes.c_double * 2
# Instantiate the array to hold the result
p_prime_result_array = DoubleArray2()

# Call the C function, passing the inputs and the output array
find_p_prime_func(p_coords[0], p_coords[1],
                  center_coords[0], center_coords[1],
                  p_prime_result_array)

# Convert the C array result back to a Python tuple
p_prime_coords = (p_prime_result_array[0], p_prime_result_array[1])

print(f"Coordinates for P: {p_coords}")
print(f"Coordinates for C: {center_coords}")
print(f"Coordinates for P' (from C function): {p_prime_coords}")


# --- Step 3: Plot the Mohr's Circle using the data ---

# Calculate radius for plotting
radius = np.sqrt((p_coords[0] - center_coords[0])**2 + (p_coords[1] - center_coords[1])**2)

# Plotting Setup
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')

# Draw the circle
mohr_circle = plt.Circle(center_coords, radius, color='skyblue', fill=False, linewidth=2)
ax.add_patch(mohr_circle)

# Plot points
ax.plot(center_coords[0], center_coords[1], 'ro', markersize=8)
ax.plot(p_coords[0], p_coords[1], 'go', markersize=8)
ax.plot(p_prime_coords[0], p_prime_coords[1], 'mo', markersize=8)

# Draw diameter
ax.plot([p_coords[0], p_prime_coords[0]], [p_coords[1], p_prime_coords[1]], 'k--')

# Annotations
ax.text(center_coords[0] + 0.2, center_coords[1] - 0.5, f'C{center_coords}', fontsize=12, color='red')
ax.text(p_coords[0] + 0.2, p_coords[1] + 0.2, f'P{p_coords}', fontsize=12, color='green')
ax.text(p_prime_coords[0] + 0.2, p_prime_coords[1] - 0.2, f"P'{p_prime_coords}", fontsize=12, color='purple')

# Formatting
ax.set_xlabel('Normal Stress (σ) [MPa]', fontsize=12)
ax.set_ylabel('Shear Stress (τ) [MPa]', fontsize=12)
ax.set_title("Mohr's Circle (P' Calculated in C)", fontsize=14)
ax.set_xlim(0, 12)
ax.set_ylim(-6, 6)
ax.grid(True, linestyle=':')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
