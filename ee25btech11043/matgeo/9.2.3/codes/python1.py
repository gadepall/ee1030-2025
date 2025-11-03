import ctypes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Load the shared library
lib_area = ctypes.CDLL("./code15.so")

# Define the argument types and return type for the C function
lib_area.calculate_integral.argtypes = [
    ctypes.c_double,  # m
    ctypes.c_double,  # c
    ctypes.c_double,  # a (lower limit)
    ctypes.c_double   # b (upper limit)
]
lib_area.calculate_integral.restype = ctypes.c_double

# Define the curve function
def f(x):
    return 1 + abs(x + 1)

# Define the integration limits
x_lower_bound = -3
x_upper_bound = 3

# The function y = 1 + |x + 1| needs to be split at x = -1
# For x < -1, x + 1 is negative, so |x + 1| = -(x + 1) = -x - 1
# y = 1 + (-x - 1) = -x
# For x >= -1, x + 1 is positive, so |x + 1| = x + 1
# y = 1 + (x + 1) = x + 2

# Case 1: x_lower_bound to -1 (if -1 is within the bounds)
area_part1 = 0.0
if x_lower_bound < -1:
    lower_limit_1 = x_lower_bound
    upper_limit_1 = min(-1, x_upper_bound) # Ensure we don't go past x_upper_bound
    # For y = -x, m = -1, c = 0
    if lower_limit_1 < upper_limit_1:
        area_part1 = lib_area.calculate_integral(-1.0, 0.0, lower_limit_1, upper_limit_1)

# Case 2: -1 to x_upper_bound (if -1 is within the bounds)
area_part2 = 0.0
if x_upper_bound > -1:
    lower_limit_2 = max(-1, x_lower_bound) # Ensure we don't start before x_lower_bound
    upper_limit_2 = x_upper_bound
    # For y = x + 2, m = 1, c = 2
    if lower_limit_2 < upper_limit_2:
        area_part2 = lib_area.calculate_integral(1.0, 2.0, lower_limit_2, upper_limit_2)

total_area = area_part1 + area_part2
print(f"The total area bounded by y = 1 + |x + 1|, x = {x_lower_bound}, x = {x_upper_bound}, and y = 0 is: {total_area:.2f}")

# Plotting the curve and the area
x = np.linspace(x_lower_bound - 1, x_upper_bound + 1, 400) # Extend range for better visualization
y = f(x)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the curve
ax.plot(x, y, 'b', linewidth=2, label=r'$y = 1 + |x + 1|$')

# Plot the boundaries
ax.axvline(x=x_lower_bound, color='gray', linestyle='--', label=f'x = {x_lower_bound}')
ax.axvline(x=x_upper_bound, color='gray', linestyle='--', label=f'x = {x_upper_bound}')
ax.axhline(y=0, color='gray', linestyle='--', label='y = 0')

# Shade the area under the curve
# Create a mask for the region of interest
x_fill = np.linspace(x_lower_bound, x_upper_bound, 200)
y_fill = f(x_fill)
verts = [(x_lower_bound, 0)] + list(zip(x_fill, y_fill)) + [(x_upper_bound, 0)]
poly = Polygon(verts, facecolor='lightgreen', edgecolor='green', alpha=0.5, label='Bounded Area')
ax.add_patch(poly)

# Add annotations for key points
ax.scatter([-1], [f(-1)], color='red', zorder=5, label='Vertex (-1, 1)')
ax.annotate(r'$(-1, 1)$', (-1, f(-1)), textcoords="offset points", xytext=(5,5), ha='left')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title(r'Region Bounded by $y = 1 + |x + 1|$, $x = -3$, $x = 3$, and $y = 0$')
ax.grid(True)
ax.legend()
ax.set_ylim(bottom=-0.5) # Ensure y=0 is visible
plt.show()
