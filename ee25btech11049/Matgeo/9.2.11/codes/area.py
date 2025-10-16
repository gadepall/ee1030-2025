# Program to plot and calculate the area under a parabola using NumPy
# Based on code by GVV Sharma
# Revised to match a specific plot style and use np.trapz for area calculation.

import numpy as np
import matplotlib.pyplot as plt

# --- Local Imports Setup ---
# This structure is maintained for consistency with your other projects,
# though the local libraries are not used in this specific script.
import sys
try:
    # Update this path to the location of your 'CoordGeo' scripts if needed
    sys.path.insert(0, '/home/sai-krishna-bakki/Desktop/Matgeo/9.2.11/codes')
    from libs.line.funcs import *
    from libs.triangle.funcs import *
    from libs.conics.funcs import *
except ImportError:
    # This block will run if the local libs are not found
    print("Generating Plot (Local libraries not found, proceeding without them)")
# --- End Local Imports Setup ---

# --- 1. Define the Parabola and Bounding Lines ---

# The curve is y^2 = 9x
def parabola_x(y):
    """Returns the x-coordinate for a given y on the parabola y^2 = 9x."""
    return (y**2) / 9

# Boundaries for the area calculation
x_min = 2
x_max = 4

# --- 2. Calculate the Area using NumPy ---

# Generate a set of points for the numerical integration.
# More points lead to a more accurate result.
num_points = 1000
x_points = np.linspace(x_min, x_max, num_points)

# Calculate the y-values for the upper and lower parts of the parabola
y_upper = np.sqrt(9 * x_points)
y_lower = -np.sqrt(9 * x_points)

# The integrand is the height of the region (upper curve - lower curve)
integrand_heights = y_upper - y_lower

# Calculate the area using NumPy's trapezoidal rule
calculated_area = np.trapz(integrand_heights, x_points)

# Print the result to the console
# The analytical solution is 32 - 8*sqrt(2)
print(f"Numerically Calculated Area (NumPy): {calculated_area:.4f}")
print(f"Analytical Solution: 32 - 8√2 ≈ {32 - 8*np.sqrt(2):.4f}")


# --- 3. Find Intersection Points for Plotting ---
y1 = np.sqrt(9 * x_min)  # y-coordinate at x=2
y2 = np.sqrt(9 * x_max)  # y-coordinate at x=4

# Points are labeled counter-clockwise from the top right
a2 = np.array([x_max, y2])
a1 = np.array([x_min, y1])
a0 = np.array([x_min, -y1])
a3 = np.array([x_max, -y2])

points = np.vstack((a0, a1, a2, a3)).T
point_labels = ['$\\mathbf{a}_0$', '$\\mathbf{a}_1$', '$\\mathbf{a}_2$', '$\\mathbf{a}_3$']


# --- 4. Set up the Plot ---
fig = plt.figure()
ax = fig.add_subplot(111)

# Generate y values for a smooth parabola curve
y_curve = np.linspace(-7, 7, 400)
x_curve = parabola_x(y_curve)

# Use the points generated for the calculation to also shade the area
x_fill = x_points
y_fill_pos = y_upper
y_fill_neg = y_lower

# --- 5. Plot the Elements ---

# Plot the parabola
ax.plot(x_curve, y_curve, 'r', label='Parabola: $y^2=9x$')

# Plot the chords (vertical lines)
ax.plot([a0[0], a1[0]], [a0[1], a1[1]], color='dodgerblue', label=f'Boundary: x={x_min}')
ax.plot([a3[0], a2[0]], [a3[1], a2[1]], color='darkorange', label=f'Boundary: x={x_max}')

# Shade the area between the curves
ax.fill_between(x_fill, y_fill_pos, y_fill_neg, color='cyan', label='Calculated Area')

# Plot and label the intersection points
ax.scatter(points[0, :], points[1, :], s=30, color='dimgray')
for i, txt in enumerate(point_labels):
    ax.annotate(txt, (points[0, i], points[1, i]), textcoords="offset points", xytext=(5,5), ha='center')

# --- 6. Formatting and Display ---

# Add a title with the calculated area
plt.title(f'Area under $y^2=9x$ from $x=2$ to $x=4$\nCalculated Area (NumPy) $\\approx$ {calculated_area:.4f}')

# Center the axes at (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Set axis limits and labels
plt.xlim(-1, 7)
plt.ylim(-7, 7)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# Add grid and legend
ax.grid(True)
ax.legend(loc='upper left')

# Show the plot
plt.show()
