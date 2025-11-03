import numpy as np
import matplotlib.pyplot as plt

# --- Setup and Calculations ---

# Define a range of x-values for the plot
x = np.linspace(-4, 6, 400)

# Rearrange the equations to solve for y
# Equation 1: 3x - 4y + 6 = 0  =>  y = (3x + 6) / 4
y1 = (3 * x + 6) / 4

# Equation 2: 3x + y - 9 = 0   =>  y = -3x + 9
y2 = -3 * x + 9

# --- Find the Vertices of the Triangle ---

# Vertex A: Intersection of the first line and the x-axis (y=0)
a = (-2, 0)

# Vertex B: Intersection of the second line and the x-axis (y=0)
b = (3, 0)

# Vertex C: Intersection of the two lines
c = (2, 3)




# --- Plotting the Graph ---

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the two lines
plt.plot(x, y1, label='3x - 4y + 6 = 0')
plt.plot(x, y2, label='3x + y - 9 = 0')

# Highlight the vertices of the triangle
vertices_x = [a[0], b[0], c[0]]
vertices_y = [a[1], b[1], c[1]]
plt.scatter(vertices_x, vertices_y, color='red', zorder=5)

# Fill the area of the triangle
plt.fill(vertices_x, vertices_y, 'gray', alpha=0.3, label='Triangle Area')

# Annotate the vertices with their coordinates and a label (A, B, C)
for i, (vx, vy) in enumerate([a, b, c]):
    label = chr(65 + i) # Generates 'A', 'B', 'C' from index 0, 1, 2
    plt.text(vx + 0.1, vy + 0.2, f'{label} ({vx}, {vy})')


# Add plot enhancements
plt.title('Graph of Linear Equations and the Formed Triangle')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axis('equal')

# Save the plot to a file
plt.savefig('triangle_plot.png')

# Show the plot
plt.show()
