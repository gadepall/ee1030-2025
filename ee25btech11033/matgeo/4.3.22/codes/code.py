
import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

c_lib=ctypes.CDLL('./code.so')

#  Define the C function's argument types and return type
c_lib.find_intersection_x.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
c_lib.find_intersection_x.restype = ctypes.c_float

# --- Problem Setup & Calculation ---

# Define the coordinates for endpoints A and B from the problem
A = np.array([1.0, -5.0])
B = np.array([-4.0, 5.0])

# Call the C function to find the x-coordinate of the division point P
Px = c_lib.find_intersection_x(
    ctypes.c_float(A[0]), # Ax
    ctypes.c_float(A[1]), # Ay
    ctypes.c_float(B[0]), # Bx
    ctypes.c_float(B[1])  # By
)

# The point of division P lies on the x-axis, so its y-coordinate is 0
P_dividing = np.array([Px, 0.0])

# As shown in the problem, the ratio is 1:1
ratio_str = "1:1"
print(f"The C function calculated the division point as: {tuple(np.round(P_dividing, 2))}")
print(f"The line segment AB is divided by the x-axis in a ratio of {ratio_str}")


# --- Plotting Code ---

def generate_line_segment(point1, point2, num_points=100):
    """Generates points to plot a line segment between two points."""
    return np.array([np.linspace(point1[i], point2[i], num_points) for i in range(2)])

# Generate the line segment for plotting
line_AB = generate_line_segment(A, B)

# Plot the line segment AB
plt.plot(line_AB[0, :], line_AB[1, :], label='Line Segment AB')

# Highlight the x-axis (the dividing line)
plt.axhline(0, color='black', linestyle='--', linewidth=1, label='X-axis (dividing line)')

# Plot the points A, B, and the calculated division point P
all_points = np.vstack((A, B, P_dividing)).T
plt.scatter(all_points[0, :], all_points[1, :], color='red', zorder=5, s=50)

# Add labels for the points
point_labels = [f'A {tuple(A)}', f'B {tuple(B)}', f'P {tuple(np.round(P_dividing,2))}']
for i, txt in enumerate(point_labels):
    plt.annotate(txt,
                 (all_points[0, i], all_points[1, i]),
                 textcoords="offset points",
                 xytext=(10, 5),
                 ha='center')

# Set plot details
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title(f'Point P divides line segment AB in a {ratio_str} ratio')
plt.legend()
plt.grid(True)
plt.axis('equal')
# Save the plot to a file
plt.savefig('../figs/fig.png')

# Display the plot
plt.show()
