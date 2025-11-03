import ctypes
import math
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Load the Compiled C Library ---

# NOTE: Change './libsimpson.so' to './libsimpson.dll' if you are on Windows.
c_lib = ctypes.CDLL('/home/shriyasnh/Desktop/matgeonew/9.2.15/codes/libsimpson.so')

# --- 2. Define the C Function Signature ---

# Get a reference to the C function
calculate_area_from_c = c_lib.calculate_area_c

# Tell Python what data types the function expects and returns.
# C signature: double calculate_area_c(double a, int n)
calculate_area_from_c.argtypes = [ctypes.c_double, ctypes.c_int]
calculate_area_from_c.restype = ctypes.c_double


# --- 3. Main Script Execution ---

# --- Parameters ---
radius = 4.0
num_intervals = 50000

# --- Calculation ---
print("Calling C function to calculate numerical area...")
# Call the C function with the specified parameters
numerical_area_c = calculate_area_from_c(radius, num_intervals)

# Calculate the exact area in Python for comparison
analytical_area = 0.5 * math.pi * radius**2

# --- Display Results ---
print(f"\n--- Results for radius = {radius} ---")
print(f"Analytical Area:      {analytical_area:.8f}")
print(f"Numerical Area (from C): {numerical_area_c:.8f}")

# --- Plotting ---
x_coords = np.linspace(-radius, radius, 400)
y_coords = np.sqrt(np.maximum(0, radius**2 - x_coords**2))

plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, label=f"$y=\sqrt{{{radius}^2-x^2}}$", color='b')
plt.fill_between(x_coords, y_coords, 0, alpha=0.2, color='b', label="Area")

plt.title(f"Semicircle Area via C & Python (radius={radius})")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.gca().set_aspect('equal', 'box')
plt.legend()

# Save the plot to a file
output_filename = "semicircle_plot_from_c.png"
plt.savefig(output_filename)

