import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define Constants and Parameters ---

# The common point of intersection for all lines
x0, y0 = 3, 2

# The angle the new lines make with the original line
angle_deg = 40.0
angle_rad = np.deg2rad(angle_deg)

# --- 2. Calculate the Slopes of the New Lines ---

# The slope of the original line, x - 2y = 3, is 1/2.
# We can find its angle 'alpha' with the x-axis.
m_orig = 0.5
alpha = np.arctan(m_orig)

# The new slopes are found by adding/subtracting 40 degrees to alpha
# using the tangent addition/subtraction formulas.
slope1 = np.tan(alpha + angle_rad)
slope2 = np.tan(alpha - angle_rad)

# --- 3. Generate Data for Plotting ---

# Create a range of x-values to plot over
x_vals = np.linspace(0, 6, 400)

# Calculate the corresponding y-values for each line
y_original = 0.5 * x_vals - 1.5  # y = (x-3)/2
y_line1 = slope1 * (x_vals - x0) + y0
y_line2 = slope2 * (x_vals - x0) + y0

# --- 4. Create and Display the Plot ---

# Set up the figure and axes
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the three lines with distinct colors and labels
ax.plot(x_vals, y_original, 'b-', label='Original Line: $x - 2y = 3$')
ax.plot(x_vals, y_line1, 'g-', label=f'Line 1 (+{angle_deg}°)')
ax.plot(x_vals, y_line2, 'm-', label=f'Line 2 (-{angle_deg}°)')

# Highlight the common intersection point
ax.plot(x0, y0, 'ro', markersize=10, label=f'Intersection Point ({x0}, {y0})')

# --- 5. Final Touches for Clarity ---

# Set the aspect ratio to 'equal' to ensure angles are displayed correctly
ax.set_aspect('equal', adjustable='box')

# Add titles, labels, and a legend
ax.set_title(f'Lines Through ({x0}, {y0}) Making a {angle_deg}° Angle', fontsize=16)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.legend(fontsize=11)
ax.grid(True)

# Show the plot
plt.show()
