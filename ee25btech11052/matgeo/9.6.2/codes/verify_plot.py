import ctypes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

# Compile and load the C library
import os
import subprocess

# Compile the C code
subprocess.run(['gcc', '-shared', '-fPIC', '-o', 'verify_plot.so', 'verify_plot.c', '-lm'])

# Load the shared library
lib = ctypes.CDLL('./verify_plot.so')

# Define the function signature
lib.calculate_area.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
lib.calculate_area.restype = ctypes.c_double

# Calculate the area using Simpson's rule
a = -np.sqrt(2)  # Lower limit
b = np.sqrt(2)   # Upper limit
n = 1000         # Number of intervals (must be even)

calculated_area = lib.calculate_area(a, b, n)

# Calculate the theoretical area from the formula
theoretical_area = (np.sqrt(2) / 6) + (9 / 4) * np.arcsin(2 * np.sqrt(2) / 3)

print("=" * 60)
print("AREA CALCULATION RESULTS")
print("=" * 60)
print(f"Calculated Area (Simpson's Rule): {calculated_area:.10f}")
print(f"Theoretical Area (Analytical):    {theoretical_area:.10f}")
print("=" * 60)

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Generate points for the circle: 4x² + 4y² = 9 => x² + y² = 9/4
theta = np.linspace(0, 2 * np.pi, 1000)
x_circle = (3/2) * np.cos(theta)
y_circle = (3/2) * np.sin(theta)

# Generate points for the parabola: x² = 4y => y = x²/4
x_parabola = np.linspace(-2.5, 2.5, 1000)
y_parabola = x_parabola**2 / 4

# Plot the curves
ax.plot(x_circle, y_circle, 'b-', linewidth=2, label='Circle: $4x^2 + 4y^2 = 9$')
ax.plot(x_parabola, y_parabola, 'orange', linewidth=2, label='Parabola: $x^2 = 4y$')

# Fill the region between curves
x_fill = np.linspace(-np.sqrt(2), np.sqrt(2), 1000)
y_circle_upper = np.sqrt(9/4 - x_fill**2)
y_parabola_fill = x_fill**2 / 4

# Create vertices for the filled region
vertices = []
for i in range(len(x_fill)):
    vertices.append([x_fill[i], y_parabola_fill[i]])
for i in range(len(x_fill)-1, -1, -1):
    vertices.append([x_fill[i], y_circle_upper[i]])

polygon = Polygon(vertices, alpha=0.4, facecolor='cyan', edgecolor='none', label='Intersection Region')
ax.add_patch(polygon)

# Mark intersection points
x1, y1 = np.sqrt(2), 0.5
x2, y2 = -np.sqrt(2), 0.5

ax.plot([x1, x2], [y1, y2], 'ro', markersize=8, zorder=5)
ax.plot([x1, x2], [y1, y2], 'ko', markersize=4, zorder=6)

# Add simple text labels for intersection points
ax.text(x1 + 0.15, y1 + 0.15, f'A({x1:.3f}, {y1:.2f})', fontsize=10, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='black'))
ax.text(x2 - 0.15, y2 + 0.15, f'B({x2:.3f}, {y2:.2f})', fontsize=10, ha='right',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='black'))

# Set labels and title
ax.set_xlabel('$x$', fontsize=14, fontweight='bold')
ax.set_ylabel('$y$', fontsize=14, fontweight='bold')
ax.set_title('Area of Circle Interior to Parabola\n$4x^2 + 4y^2 = 9$ interior to $x^2 = 4y$', 
             fontsize=15, fontweight='bold', pad=20)

# Set grid and legend
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

# Set axis limits and aspect ratio
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-1.8, 2.0)
ax.set_aspect('equal')

# Add minor ticks
ax.minorticks_on()
ax.grid(which='minor', alpha=0.1)

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('/home/shriyasnh/Desktop/matgeonew/9.6.2/figs/area_plot.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

# Verification section
print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)
print(f"Intersection points: A = (√2, 1/2) = ({np.sqrt(2):.6f}, 0.5)")
print(f"                     B = (-√2, 1/2) = ({-np.sqrt(2):.6f}, 0.5)")
print(f"\nIntegration limits: [{-np.sqrt(2):.6f}, {np.sqrt(2):.6f}]")
print(f"Number of intervals: {n}")
print(f"Method: Simpson's 1/3 Rule")
print("=" * 60)