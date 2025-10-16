# Program to plot the area under a parabola using a C backend for calculation.
# Based on code by GVV Sharma
# Python script by user, C integration by Gemini

import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys

# --- Local Imports Setup ---
# Update this path to the location of your 'CoordGeo' scripts

try:
    from libs.line.funcs import *
    from libs.triangle.funcs import *
    from libs.conics.funcs import *
except ImportError:
    print(" ")
# --- End Local Imports Setup ---


# --- 1. Compile and Load the C Library ---

# Define file names
c_source = "area_lib.c"
lib_name = "area_lib.so"

# Compilation command (for Linux/macOS). For Windows, this would be different.


# Load the compiled shared library
try:
    area_lib = ctypes.CDLL(os.path.abspath(lib_name))
except OSError as e:
    print(f"Error loading shared library: {e}")
    sys.exit(1)


# --- 2. Define the C function signature for Python ---

# Get the function from the library
trapezoidal_area_c = area_lib.trapezoidal_area

# Specify the argument types (double, double, int)
trapezoidal_area_c.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
# Specify the return type (double)
trapezoidal_area_c.restype = ctypes.c_double


# --- 3. Define Parabola, Boundaries and Calculate Area ---

# The curve is y^2 = 9x
def parabola_x(y):
    """Returns the x-coordinate for a given y on the parabola y^2 = 9x."""
    return (y**2) / 9

# Boundaries
x_min = 2
x_max = 4

# Call the C function to get the area for the first quadrant
area_first_quadrant = trapezoidal_area_c(ctypes.c_double(x_min), ctypes.c_double(x_max), ctypes.c_int(1000))
# The total area is symmetric, so we double the result
total_area = 2 * area_first_quadrant
print(f"The calculated total area (from C function) is: {total_area}")


# --- 4. Find Intersection Points for Plotting ---
y1 = np.sqrt(9 * x_min)
y2 = np.sqrt(9 * x_max)
a2 = np.array([x_max, y2])
a1 = np.array([x_min, y1])
a0 = np.array([x_min, -y1])
a3 = np.array([x_max, -y2])
points = np.vstack((a0, a1, a2, a3)).T
point_labels = ['$\\mathbf{a}_0$', '$\\mathbf{a}_1$', '$\\mathbf{a}_2$', '$\\mathbf{a}_3$']


# --- 5. Set up the Plot ---
fig = plt.figure()
ax = fig.add_subplot(111)

# Generate data for plotting
y_curve = np.linspace(-7, 7, 400)
x_curve = parabola_x(y_curve)
x_fill = np.linspace(x_min, x_max, 100)
y_fill_pos = np.sqrt(9 * x_fill)
y_fill_neg = -np.sqrt(9 * x_fill)

# Plot the elements
ax.plot(x_curve, y_curve, 'r', label='Parabola')
ax.plot([a0[0], a1[0]], [a0[1], a1[1]], color='dodgerblue', label='Chord')
ax.plot([a3[0], a2[0]], [a3[1], a2[1]], color='darkorange', label='Chord')
ax.fill_between(x_fill, y_fill_pos, y_fill_neg, color='cyan', label=f'Area $\\approx$ {total_area:.4f}')
ax.scatter(points[0, :], points[1, :], s=30, color='dimgray')
for i, txt in enumerate(point_labels):
    ax.annotate(txt, (points[0, i], points[1, i]), textcoords="offset points", xytext=(5,5), ha='center')

# --- 6. Formatting and Display ---
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.xlim(-1, 7)
plt.ylim(-7, 7)
ax.grid(True)
ax.legend(loc='upper left')
plt.show()

