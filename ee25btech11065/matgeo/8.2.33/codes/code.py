import ctypes
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

# --- 1. C Library Setup ---

# Define the name of the shared library file.
LIB_NAME = './area_calculator.so'

# Check if the compiled C library exists. If not, provide instructions and exit.
if not os.path.exists(LIB_NAME):
    print(f"Error: '{os.path.basename(LIB_NAME)}' not found.")
    print("Please compile the 'area_calculator.c' file from the Canvas first.")
    print("Command: gcc -shared -o area_calculator.so -fPIC area_calculator.c")
    sys.exit()

# Load the shared library from the current directory.
c_lib = ctypes.CDLL(LIB_NAME)

# --- 2. Define C Function Signature ---

# Get a handle to the function from the C library.
calculate_area_func = c_lib.calculate_circular_sector_area

# Specify the return type of the C function. 
# In C, it's a 'double', which corresponds to 'c_double' in ctypes.
calculate_area_func.restype = ctypes.c_double

# --- 3. Call C Function and Print Results ---

print("Calling the C function from the shared library...")

# Call the function. No arguments are needed.
area_result = calculate_area_func()

print(f"The area calculated by the C function is: {area_result:.4f}\n")

# --- 4. Prepare for Plotting ---

# Define parameters for the plot
radius = 2.0
theta_line = np.pi / 6  # Angle of the line x = sqrt(3)y is 30 degrees or pi/6 radians

# Create data for the circle
theta_circle = np.linspace(0, 2 * np.pi, 200)
x_circle = radius * np.cos(theta_circle)
y_circle = radius * np.sin(theta_circle)

# Create data for the line
x_line = np.linspace(0, 3, 100)
y_line = x_line / np.sqrt(3)

# --- 5. Plotting ---

fig, ax = plt.subplots(figsize=(8, 8))

# Plot the circle and the line
ax.plot(x_circle, y_circle, label=r'$x^2 + y^2 = 4$')
ax.plot(x_line, y_line, label=r'$x = \sqrt{3}y$')

# Create and add the shaded region (a wedge/circular sector)
# The wedge goes from angle 0 to pi/6 (30 degrees)
wedge = Wedge(center=(0, 0), r=radius, theta1=0, theta2=np.degrees(theta_line), 
              facecolor='gray', alpha=0.4)
ax.add_patch(wedge)

# --- 6. Formatting the Plot ---

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Area of the Enclosed Region', fontsize=14)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.legend()
plt.show()


