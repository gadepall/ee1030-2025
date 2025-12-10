import matplotlib.pyplot as plt
import numpy as np

# --- 1. Set up the data for the parabola ---
# Define the quadratic function
def parabola(x):
    return x**2 - 7*x - 60

# Generate a range of x-values to create a smooth curve
# A range from -15 to 25 is sufficient to show the curve's shape and intercepts.
x = np.linspace(-15, 25, 400)
# Calculate the corresponding y-values
y = parabola(x)

# --- 2. Create the plot ---
# Set the figure size to be similar to the example (somewhat square)
plt.figure(figsize=(8, 8))

# Plot the parabola
# Use a LaTeX string for the equation in the label for proper formatting
plt.plot(x, y, label=r'$y = x^2 - 7x - 60$', linewidth=2)

# Plot the horizontal line at y=0 to represent the x-axis
plt.axhline(0, color='tab:orange')

# --- 3. Define and plot the intersection points ---
# Coordinates for points A and B
x_intercepts = {
    'A': (12, 0),
    'B': (-5, 0)
}

# Plot Point A (12, 0)
# This point has a blue edge and a red face
plt.scatter(
    x_intercepts['A'][0], 
    x_intercepts['A'][1], 
    s=100,                 # size of the marker
    facecolors='red',      # inner color
    edgecolors='darkblue', # border color
    linewidth=2,
    zorder=5               # zorder ensures points are drawn on top of the lines
)

# Plot Point B (-5, 0)
# This point is a yellow diamond
plt.scatter(
    x_intercepts['B'][0], 
    x_intercepts['B'][1],
    s=90,                  # size of the marker
    marker='D',            # 'D' for diamond shape
    color='gold',          # color of the diamond
    zorder=5
)

# --- 4. Add annotations (text labels) for the points ---
# Annotation for Point A
plt.annotate(
    'A\n(12, 0)', 
    xy=x_intercepts['A'], 
    xytext=(12, 5),        # Position of the text
    fontweight='bold', 
    ha='center'            # Horizontal alignment
)

# Annotation for Point B
plt.annotate(
    'B\n(-5, 0)', 
    xy=x_intercepts['B'], 
    xytext=(-5, 5),        # Position of the text
    fontweight='bold', 
    ha='center'            # Horizontal alignment
)

# --- 5. Finalize the plot ---
# Set the axis limits to match the provided image
plt.xlim(-50, 50)
plt.ylim(-75, 30)

# Add a grid
plt.grid(True)

# Add the legend to the lower-left corner
plt.legend(loc='lower left', fontsize=12)
plt.savefig("..figs/fig.png")
# Display the plot
plt.show()
