# File: plot_combined.py
import numpy as np
import matplotlib.pyplot as plt

# Hardcoded list of ALL m values that produce an integer x-coordinate
all_m_values = [-2, -1, -0.5, 0.5]

print(f"Plotting a single combined graph for m values: {all_m_values}")

# --- Key Change 1: Create the figure and axes ONCE, before the loop ---
plt.figure(figsize=(10, 8))

# Define the x-range for the plot
x_range = np.linspace(-10, 10, 400)

# --- Key Change 2: Plot the main line ONCE, before the loop ---
# Equation of the first line: 3x + 4y = 9  =>  y = (9 - 3x) / 4
y1 = (9 - 3 * x_range) / 4
plt.plot(x_range, y1, label='$3x + 4y = 9$', color='black', linewidth=2.5, zorder=5)

# Loop through each value of m to plot the other lines
for m in all_m_values:
    # Equation of the second line: y = mx + 1
    y2 = m * x_range + 1
    
    # Calculate the intersection point
    x_intersect = 5 / (3 + 4 * m)
    y_intersect = m * x_intersect + 1
    
    # Plot the line for the current m
    line = plt.plot(x_range, y2, label=f'$y = {m}x + 1$')
    
    # Plot the intersection point, matching the color of the line
    plt.plot(x_intersect, y_intersect, 'o', markersize=8, color=line[0].get_color(), zorder=10)

# --- Key Change 3: Formatting and showing the plot is done ONCE, after the loop ---
plt.title('Combined Plot of Line Intersections')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')

# Show the single, combined plot
plt.savefig('2.png')
plt.show()
