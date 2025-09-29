import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared object for triangle median equation
triangle_lib = ctypes.CDLL("./trianglefun.so")

# Define the function prototype for median_equation
triangle_lib.median_equation.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]

# Triangle vertices (same as in C main program)
Ax, Ay = 2, 5
Bx, By = -4, 9
Cx, Cy = -2, -1

# Prepare a ctypes buffer to store the median equation string
buffer = ctypes.create_string_buffer(50)

# Call C function
triangle_lib.median_equation(Ax, Ay, Bx, By, Cx, Cy, buffer)

# Get median equation string from buffer
median_eqn = buffer.value.decode('utf-8')

# Calculate midpoint M of BC (for plotting)
M = np.array([(Bx + Cx) / 2, (By + Cy) / 2])
A = np.array([Ax, Ay])

# Plot triangle
plt.figure(figsize=(6,6))
triangle_points = np.array([A, [Bx, By], [Cx, Cy], A])
plt.plot(triangle_points[:,0], triangle_points[:,1], 'k-', label='Triangle ABC')

# Plot vertices
plt.plot(Ax, Ay, 'ro')
plt.plot(Bx, By, 'ro')
plt.plot(Cx, Cy, 'ro')

# Label vertices
plt.text(Ax+0.2, Ay, f'A({Ax},{Ay})', fontsize=12, color='red')
plt.text(Bx+0.2, By, f'B({Bx},{By})', fontsize=12, color='red')
plt.text(Cx+0.2, Cy, f'C({Cx},{Cy})', fontsize=12, color='red')

# Plot median from A to midpoint M
plt.plot([Ax, M[0]], [Ay, M[1]], 'b--', linewidth=2, label='Median AM')

# Label midpoint M
plt.plot(M[0], M[1], 'go')
plt.text(M[0]+0.2, M[1], f'M({M[0]:.1f},{M[1]:.1f})', fontsize=12, color='green')

# Position to place equation near the median line midpoint
mid_x = (Ax + M[0]) / 2
mid_y = (Ay + M[1]) / 2

# Show median equation at midpoint
plt.text(mid_x, mid_y, median_eqn, fontsize=14, color='blue')

# Settings
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title('Triangle ABC with Median from A')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(-6, 4)
plt.ylim(-3, 11)

# Save and show plot
plt.savefig('triangle_median_eqonline_from_c.png')
plt.show()
