import ctypes
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Load C library and define function signature ---

# Load the shared library directly.
# This assumes 'libtangent.so' is in the same directory.
lib = ctypes.CDLL("./libverify_plot.so")

# Define the argument and return types for the C function
calculate_tangent_points = lib.calculate_tangent_points
calculate_tangent_points.argtypes = [ctypes.c_double, ctypes.c_double,
                                     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
calculate_tangent_points.restype = ctypes.c_int

# --- 2. Call the C function to get the coordinates ---

# Define problem parameters
radius = 4.0
p_x = 6.0

# Create C-compatible double variables to store the results
q1_x, q1_y = ctypes.c_double(), ctypes.c_double()
q2_x, q2_y = ctypes.c_double(), ctypes.c_double()

# Call the function from the C library
result = calculate_tangent_points(radius, p_x,
                                  ctypes.byref(q1_x), ctypes.byref(q1_y),
                                  ctypes.byref(q2_x), ctypes.byref(q2_y))


# Extract the float values from the ctypes objects for plotting
q1 = (q1_x.value, q1_y.value)
q2 = (q2_x.value, q2_y.value)
P = (p_x, 0)
O = (0, 0)

# --- 3. Plot the results using matplotlib ---

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Draw the circle with a solid line
circle = plt.Circle(O, radius, color='blue', fill=False, linestyle='-', label='Circle $x^2+y^2=16$')
ax.add_artist(circle)

# Plot the points
ax.plot(O[0], O[1], 'ko', markersize=8, label=f'Center O({O[0]},{O[1]})')
ax.plot(P[0], P[1], 'ro', markersize=8, label=f'Point P({P[0]},{P[1]})')
ax.plot(q1[0], q1[1], 'go', markersize=8, label=f'Contact Point $q_1$')
ax.plot(q2[0], q2[1], 'go', markersize=8, label=f'Contact Point $q_2$')

# Draw the tangent lines
ax.plot([P[0], q1[0]], [P[1], q1[1]], 'r-')
ax.plot([P[0], q2[0]], [P[1], q2[1]], 'r-')

# Add annotations for the coordinates, matching PDF notation
ax.text(P[0] + 0.2, P[1], f'P({P[0]}, {P[1]})')
ax.text(O[0] - 1, O[1] - 0.5, f'O({O[0]}, {O[1]})')
ax.text(q1[0] + 0.2, q1[1], f'$q_1$ ({q1[0]:.2f}, {q1[1]:.2f})')
ax.text(q2[0] + 0.2, q2[1], f'$q_2$ ({q2[0]:.2f}, {q2[1]:.2f})')

# --- 4. Formatting the plot ---

# Set plot limits to ensure the entire circle is visible
ax.set_xlim(-5, 8)
ax.set_ylim(-6, 6)
ax.set_aspect('equal', adjustable='box')

# Add grid, title, and labels
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_title('Tangents to a Circle from an External Point')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.legend()

# Save the plot as a PNG file
plt.savefig('/home/shriyasnh/Desktop/matgeonew/10.6.8/figs/tangents_plot.png')

# Display the plot
plt.show()

