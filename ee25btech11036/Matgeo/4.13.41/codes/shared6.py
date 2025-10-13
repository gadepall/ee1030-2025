import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled shared library
lib = ctypes.CDLL('./libpara.so')
lib.parallelogram_area.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.parallelogram_area.restype = ctypes.c_double

# Slopes
m = 1
n = -1

# Function to get intersection of two lines: y = m1 x + c1 and y = m2 x + c2
def line_intersection(m1, c1, m2, c2):
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1
    return x, y

# Calculate all four vertices (intersections)
P1 = line_intersection(m, 0, n, 0)       # y=mx and y=nx
P2 = line_intersection(m, 0, n, 1)       # y=mx and y=nx+1
P3 = line_intersection(m, 1, n, 1)       # y=mx+1 and y=nx+1
P4 = line_intersection(m, 1, n, 0)       # y=mx+1 and y=nx

# Convert to numpy arrays for vector operations
P1 = np.array(P1)
P2 = np.array(P2)
P3 = np.array(P3)
P4 = np.array(P4)

# Compute side vectors for area calculation (two adjacent sides from P1)
vec1 = P2 - P1
vec2 = P4 - P1

# Call the C function for area
area = lib.parallelogram_area(vec1[0], vec1[1], vec2[0], vec2[1])

# ----- Plotting Section -----

# X range for lines plotting
x_vals = np.linspace(-2, 2, 400)

# Lines y = mx and y = mx + 1
y_m = m * x_vals
y_m1 = m * x_vals + 1

# Lines y = nx and y = nx + 1
y_n = n * x_vals
y_n1 = n * x_vals + 1

plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_m, label=r'$y = mx$', color='blue')
plt.plot(x_vals, y_m1, label=r'$y = mx + 1$', linestyle='--', color='blue')
plt.plot(x_vals, y_n, label=r'$y = nx$', color='red')
plt.plot(x_vals, y_n1, label=r'$y = nx + 1$', linestyle='--', color='red')

# Parallelogram vertices for plotting (close the polygon by adding P1 again)
vertices_x = [P1[0], P2[0], P3[0], P4[0], P1[0]]
vertices_y = [P1[1], P2[1], P3[1], P4[1], P1[1]]

# Plot parallelogram
plt.plot(vertices_x, vertices_y, 'k-', linewidth=2, label='Parallelogram')
plt.fill(vertices_x, vertices_y, color='gray', alpha=0.3)

# Label vertices
for i, (xv, yv) in enumerate(zip(vertices_x[:-1], vertices_y[:-1]), 1):
    plt.text(xv, yv, f'P{i}', fontsize=12, ha='right', va='bottom')

# Show area on plot
plt.text(-1.5, 1.5, f'Area = {area:.4f}', fontsize=14, color='green',
         bbox=dict(facecolor='white', alpha=0.8))

# Axis formatting
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title('Parallelogram formed by lines $y=mx$, $y=mx+1$, $y=nx$, $y=nx+1$\n(Area via C shared library)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axis('equal')
plt.xlim(-2, 2)
plt.ylim(-2, 2)

plt.show()

