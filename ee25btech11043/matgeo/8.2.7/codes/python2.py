import numpy as np
import matplotlib.pyplot as plt

# Function to generate points for a line segment
def line_gen_num(A, B, num_points):
    A = np.array(A).flatten()
    B = np.array(B).flatten()
    t = np.linspace(0, 1, num_points)
    points = np.array([(1-t) * A[0] + t * B[0], (1-t) * A[1] + t * B[1]])
    return points

# Function to generate points for an ellipse (modified from circ_gen)
def ellipse_gen(center, a, b, num_points=100):
    center = np.array(center).flatten()
    theta = np.linspace(0, 2*np.pi, num_points)
    x = center[0] + b * np.cos(theta) # Note: b is for x-axis, a is for y-axis in this ellipse
    y = center[1] + a * np.sin(theta)
    return np.array([x, y])

# --- Analyze the Ellipse: 16x^2 + y^2 = 16 ---
# Standard form: x^2/b^2 + y^2/a^2 = 1
# Divide by 16: x^2/1 + y^2/16 = 1
a_val = 4.0 # Major semi-axis along y
b_val = 1.0 # Minor semi-axis along x
center = np.array([0.0, 0.0])

# Calculate properties
c_val = np.sqrt(a_val**2 - b_val**2) # Distance from center to focus
eccentricity = c_val / a_val
latus_rectum_length = (2 * b_val**2) / a_val

# Vertices (along major axis, y-axis)
vertex1 = np.array([0.0, a_val])
vertex2 = np.array([0.0, -a_val])

# Foci (along major axis, y-axis)
focus1 = np.array([0.0, c_val])
focus2 = np.array([0.0, -c_val])

# Directrices (equations are y = +/- a/e)
directrix_y = a_val / eccentricity

print(f"--- Conic Section Properties (Ellipse: 16x^2 + y^2 = 16) ---")
print(f"Center: ({center[0]:.0f}, {center[1]:.0f})")
print(f"Vertices: ({vertex1[0]:.0f}, {vertex1[1]:.0f}) and ({vertex2[0]:.0f}, {vertex2[1]:.0f})")
print(f"Foci: ({focus1[0]:.2f}, {focus1[1]:.2f}) and ({focus2[0]:.2f}, {focus2[1]:.2f})")
print(f"Eccentricity: {eccentricity:.4f}")
print(f"Axis of the conic section: y-axis (x=0) is the major axis")
print(f"Equation of Directrices: y = {directrix_y:.2f} and y = {-directrix_y:.2f}")
print(f"Length of Latus Rectum: {latus_rectum_length:.2f}")


# --- Plotting ---
# Increase figure width to make space for the legend
plt.figure(figsize=(12, 10)) # Increased width from 10 to 12
ax = plt.gca()

# Generate points for the ellipse
x_ellipse = ellipse_gen(center, a_val, b_val)
plt.plot(x_ellipse[0,:], x_ellipse[1,:], "g-", linewidth=2, label='Ellipse $16x^2 + y^2 = 16$')

# Plot Center
plt.scatter(center[0], center[1], color='green', s=50, zorder=5, label='Center (0,0)')
# No annotation for center to avoid clutter, as it's at origin and labelled in legend.

# Plot Vertices
plt.scatter(vertex1[0], vertex1[1], color='black', s=30, zorder=5, label=f'Vertices (0, $\\pm${a_val:.0f})')
plt.scatter(vertex2[0], vertex2[1], color='black', s=30, zorder=5)
plt.annotate(f'(0, {vertex1[1]:.0f})', (vertex1[0],vertex1[1]), textcoords="offset points", xytext=(3, 0), ha='left', color='black', weight='bold') # Adjusted xytext
plt.annotate(f'(0, {vertex2[1]:.0f})', (vertex2[0],vertex2[1]), textcoords="offset points", xytext=(3, -4), ha='left', color='black', weight='bold') # Adjusted xytext


# Plot Foci
plt.scatter(focus1[0], focus1[1], color='blue', s=30, zorder=5, label=f'Foci (0, $\\pm${focus1[1]:.2f})')
plt.scatter(focus2[0], focus2[1], color='blue', s=30, zorder=5)
plt.annotate(f'(0, {focus1[1]:.2f})', (focus1[0],focus1[1]), textcoords="offset points", xytext=(0, -15), ha='left', color='blue', weight='bold') # Adjusted xytext
plt.annotate(f'(0, {focus2[1]:.2f})', (focus2[0],focus2[1]), textcoords="offset points", xytext=(0, 10), ha='left', color='blue', weight='bold') # Adjusted xytext


# Plot Directrices
x_lim = np.array([-b_val * 2.5, b_val * 2.5]) # Adjust x-limits for directrix lines, slightly wider
plt.plot(x_lim, [directrix_y, directrix_y], 'r', linewidth=1.5, label=f'Directrices y = $\\pm${directrix_y:.2f}')
plt.plot(x_lim, [-directrix_y, -directrix_y], 'r', linewidth=1.5)

# Plot Latus Rectum (at each focus, perpendicular to major axis)
lr_half = latus_rectum_length / 2
plt.plot([-lr_half, lr_half], [focus1[1], focus1[1]], 'g-', linewidth=2, label=f'Latus Rectum Length={latus_rectum_length:.2f}')
plt.plot([-lr_half, lr_half], [focus2[1], focus2[1]], 'g-', linewidth=2)


ax.set_aspect('equal', adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Properties of the Ellipse $16x^2 + y^2 = 16$')
plt.grid(True)

# Place the legend outside the plot area
plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5), fontsize='medium') # Moves legend to the right
# bbox_to_anchor=(1.05, 0.5) means 5% to the right of the plot, vertically centered.

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)

# Adjust plot limits if necessary to ensure all annotations and elements are visible
plt.xlim(-2.5, 2.5) # Slightly wider X-axis to make space for annotations
plt.ylim(-5, 5)   # Slightly taller Y-axis if needed

# Use tight_layout to automatically adjust plot parameters for a tight layout.
plt.tight_layout(rect=[0, 0, 0.8, 1]) # rect=[left, bottom, right, top] - leaves space on the right for legend

# Save the figure
plt.savefig("fig2.png")
plt.show()

print("\nFigure saved as fig2.png")
