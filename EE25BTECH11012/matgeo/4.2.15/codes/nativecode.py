import matplotlib.pyplot as plt
import numpy as np

# --- 1. Vector Calculation ---
# The equation of the line is y = 2x.
# The standard form is Ax + By + C = 0, which is 2x - y = 0.
A = 2
B = -1

# The normal vector is <A, B>. It's perpendicular to the line.
normal_vector = np.array([A, B])

# The direction vector is <-B, A>. It's parallel to the line.
direction_vector = np.array([-B, A])

print(f"Line Equation: y = 2x")
print("-" * 25)
print(f"Direction Vector: {tuple(direction_vector)}")
print(f"Normal Vector:    {tuple(normal_vector)}")


# --- 2. Plotting ---

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(8, 8))

# Generate x values for our line
x_vals = np.linspace(-2.5, 2.5, 100)
# Calculate the corresponding y values for the line y = 2x
y_vals = 2 * x_vals

# Plot the main line
ax.plot(x_vals, y_vals, label='Line: y = 2x', color='blue', zorder=1)

# Plot the vectors as arrows starting from the origin (0,0)
# The 'quiver' function is used to plot arrows.

# Plot the Direction Vector (green)
ax.quiver(0, 0, direction_vector[0], direction_vector[1],
          angles='xy', scale_units='xy', scale=1,
          color='green', label=f'Direction Vector: {tuple(direction_vector)}', zorder=2)

# Plot the Normal Vector (red)
ax.quiver(0, 0, normal_vector[0], normal_vector[1],
          angles='xy', scale_units='xy', scale=1,
          color='red', label=f'Normal Vector: {tuple(normal_vector)}', zorder=2)


# --- 3. Customization and Labels ---

# Set the aspect ratio of the plot to be equal, so 90-degree angles look correct
ax.set_aspect('equal')

# Set the limits for the x and y axes
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

# Move the x and y axes to the center of the plot
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Add a grid for better readability
ax.grid(True, linestyle='--')

# Add a title and a legend
ax.set_title("Line y=2x with its Direction and Normal Vectors", fontsize=14)
ax.legend(loc='upper left')

# Display the plot
plt.show()