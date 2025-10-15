import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Part 1: Call the C Shared Library to Find the Roots ---

# Define the path to the shared library
lib_path = './libroots.so'

# Load the shared library
# Note: This will raise an OSError if the file is not found.
# Ensure 'libroots.so' is in the same directory.
solver_lib = ctypes.CDLL(lib_path)

# Define the argument types for the C function
# void find_roots(double a, double b, double c, double* root1, double* root2)
solver_lib.find_roots.argtypes = [
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
solver_lib.find_roots.restype = None

# Create two double variables in Python to hold the results from C
root1 = ctypes.c_double()
root2 = ctypes.c_double()

# Coefficients for the equation x^2 + 3x - 10 = 0
a, b, c = 1.0, 3.0, -10.0

# Call the C function to find the roots
solver_lib.find_roots(a, b, c, ctypes.byref(root1), ctypes.byref(root2))

# Extract the calculated roots into a regular Python list
roots_from_c = [root1.value, root2.value]
print(f" Roots successfully retrieved from C library: {roots_from_c[0]} and {roots_from_c[1]}")


# --- Part 2: Plot the Parabola Using the Roots from C ---

# Define the parabola function
def parabola(x):
    return a*x**2 + b*x + c

# Calculate the vertex of the parabola
vertex_x = -b / (2 * a)
vertex_y = parabola(vertex_x)

# Generate x-values for a smooth curve
x_vals = np.linspace(min(roots_from_c) - 3, max(roots_from_c) + 3, 400)
y_vals = parabola(x_vals)

# Create the plot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 9))

# Plot the parabola itself
ax.plot(x_vals, y_vals, label=r'$y = x^2 + 3x - 10$', color='royalblue', linewidth=2.5)
ax.axhline(0, color='black', linestyle='--', linewidth=1)
ax.axvline(0, color='black', linestyle='--', linewidth=1)

# Highlight the roots on the plot using the values from the C function
ax.plot(roots_from_c, [0, 0], 'o', color='crimson', markersize=10, zorder=5, 
        label=f'Roots (from C): x = {roots_from_c[0]:.0f}, {roots_from_c[1]:.0f}')

# Highlight the vertex
ax.plot(vertex_x, vertex_y, 'o', color='forestgreen', markersize=10, zorder=5,
        label=f'Vertex: ({vertex_x:.2f}, {vertex_y:.2f})')

# Add annotations for clarity
ax.annotate(f'Root: {roots_from_c[0]:.0f}', xy=(roots_from_c[0], 0), xytext=(roots_from_c[0]-1, 5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))
ax.annotate(f'Root: {roots_from_c[1]:.0f}', xy=(roots_from_c[1], 0), xytext=(roots_from_c[1]-1, 5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))

# Set labels and title
ax.set_xlabel('X-axis', fontsize=14)
ax.set_ylabel('Y-axis', fontsize=14)
ax.set_title('Parabola with Roots Calculated by C Library', fontsize=18, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(True)

# Save and show the plot
plt.savefig("Figure_1.png")
plt.show()


