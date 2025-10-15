import numpy as np
import matplotlib.pyplot as plt

# Define the parabola function
def parabola(x):
    return x**2 + 3*x - 10

# Generate a range of x-values for the plot
x = np.linspace(-8, 5, 400)
y = parabola(x)

# The roots of the equation x^2 + 3x - 10 = 0
roots = [-5, 2]
root_y = [0, 0]

# Coordinates of the vertex
vertex_x = -1.5
vertex_y = parabola(vertex_x)

# Create the plot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the parabola
ax.plot(x, y, label=r'$y = x^2 + 3x - 10$', color='royalblue', linewidth=2)

# Add a horizontal line for the x-axis
ax.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax.axvline(0, color='black', linestyle='--', linewidth=0.8)

# Highlight the roots on the plot
ax.plot(roots, root_y, 'o', color='crimson', markersize=10, zorder=5, 
        label=f'Roots at x = {roots[0]} and x = {roots[1]}')

# Highlight the vertex
ax.plot(vertex_x, vertex_y, 'o', color='forestgreen', markersize=10, zorder=5,
        label=f'Vertex at ({vertex_x:.2f}, {vertex_y:.2f})')

# Set labels and title for clarity
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_title('Parabola Intersecting the x-axis', fontsize=16, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True)

# Save the figure and display the plot
plt.savefig("Figure_2.png")
plt.show()
