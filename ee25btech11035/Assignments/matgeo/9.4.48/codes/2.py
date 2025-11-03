import numpy as np
import matplotlib.pyplot as plt

# Define the quadratic function for the parabola
def parabola(x):
    return x**2 + 2*x - 143

roots = [11, -13]
y_roots = [0, 0] # y-coordinate is 0 for roots

vertex_x = -2 / (2 * 1)
vertex_y = parabola(vertex_x)

# Create a range of x-values that includes the roots and vertex
x_values = np.linspace(-20, 20, 400)
y_values = parabola(x_values)

plt.figure(figsize=(10, 8))

# Plot the parabola curve
plt.plot(x_values, y_values, label='$y = x^2 + 2x - 143$', color='blue')

# Plot and label the roots
plt.plot(roots, y_roots, 'ro', markersize=8, label='Roots (x-intercepts)')
plt.text(roots[0], 15, f'Root: ({roots[0]}, 0)', ha='center', color='red')
plt.text(roots[1], 15, f'Root: ({roots[1]}, 0)', ha='center', color='red')

# Plot and label the vertex
plt.plot(vertex_x, vertex_y, 'go', markersize=8, label='Vertex')
plt.text(vertex_x, vertex_y - 20, f'Vertex: ({vertex_x}, {vertex_y})', ha='center', color='green')

# Add a horizontal line for the x-axis
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)

plt.title('Parabola and its Roots', fontsize=16)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.grid(True, linestyle=':')
plt.legend()

# Save and show the plot
plt.savefig('2.png')
plt.show()