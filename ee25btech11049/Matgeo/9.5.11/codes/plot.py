# A Python script to solve for the roots of a quadratic equation and plot the result.

import numpy as np
import matplotlib.pyplot as plt

# --- 1. SOLVE FOR THE ROOTS ---

# Define the coefficients of the equation: 9x^2 - 155x - 500 = 0
coefficients = [9, -155, -500]

# Use numpy's `roots` function to find the solutions
roots = np.roots(coefficients)

# Print the calculated roots
print("--- Root Calculation ---")
print(f"The equation is: {coefficients[0]}x^2 + {coefficients[1]}x + {coefficients[2]} = 0")
print(f"The calculated roots are: x1 = {roots[0]:.4f} and x2 = {roots[1]:.4f}\n")


# --- 2. GENERATE THE PLOT ---

# Setup the plot with a specific size
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# Define the parabola function and generate x and y points for plotting
x_vals = np.linspace(-10, 30, 500)
y_vals = 9*x_vals**2 - 155*x_vals - 500

# Plot the parabola curve
ax.plot(x_vals, y_vals, label='$y = 9x^2 - 155x - 500$')

# Plot the x-axis, styled like the example
ax.axhline(0, color='orange', linewidth=1.5)

# Define the intersection points using the roots we calculated
# Sort the roots to consistently label the left one 'B' and the right one 'A'
sorted_roots = np.sort(roots)
roots_y = np.zeros_like(sorted_roots)
point_labels = ['B', 'A']
colors = ['gold', '#9400D3'] # Colors styled like your example

# Plot the intersection points as colored dots
ax.scatter(sorted_roots, roots_y, c=colors, s=50, zorder=5, edgecolor='black')

# Add labels for the intersection points (A and B)
for i in range(len(sorted_roots)):
    # --- CORRECTED CODE ---
    # Line 1: The bold letter (A or B) using LaTeX formatting
    line1 = f"$\\mathbf{{{point_labels[i]}}}$"
    
    # Line 2: The coordinates
    line2 = f"({sorted_roots[i]:.2f}, {roots_y[i]:.0f})"
    
    # Join the two lines with a newline character
    label = f"{line1}\n{line2}"
    # --- END CORRECTION ---

    ax.annotate(label,
                (sorted_roots[i], roots_y[i]),
                textcoords="offset points",
                xytext=(0, 15),
                ha='center',
                fontsize=10,
                fontweight='bold')

# --- 3. FINALIZE AND DISPLAY THE PLOT ---

# Add a grid, legend, and labels
ax.grid(True)
ax.legend(loc='lower left')
ax.set_title('Parabola with x-intercepts', fontsize=16)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# Set the viewing window for the plot
ax.set_xlim(-15, 35)
ax.set_ylim(-1250, 250)

# Display the plot in a new window
print("--- Plot Generation ---")
print("Displaying plot...")
plt.show()
