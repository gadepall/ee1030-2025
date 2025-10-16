import ctypes
import subprocess
import os
import platform
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# --- Part 1: Calculate the Solution using NumPy ---

# Define the coefficient matrix A and the constant vector B
A = np.array([
    [5, -1, 4],
    [2,  3, 5],
    [5, -2, 6]
])
B = np.array([5, 2, -1])

# Use numpy.linalg.solve() to find the intersection point
try:
    solution = np.linalg.solve(A, B)
    x_int, y_int, z_int = solution
    print(f"🐍 Python calculated intersection point: ({x_int:.0f}, {y_int:.0f}, {z_int:.0f})")
except np.linalg.LinAlgError:
    print("The system of equations has no unique solution.")
    exit()


# --- Part 2: Compile and Call C Function using ctypes ---

c_source_file = "points.c"
if platform.system() == "Windows":
    lib_file = "points.dll"
else:
    lib_file = "points.so"

try:
    # Compile the C code into a shared library
    subprocess.run(["gcc", "-shared", "-o", lib_file, "-fPIC", c_source_file], check=True)
    
    # Load the shared library
    c_lib = ctypes.CDLL(os.path.join(os.getcwd(), lib_file))

    # Define the argument types for the C function (three integers)
    c_lib.process_point.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
    c_lib.process_point.restype = None

    # Call the C function, passing the values calculated by NumPy
    # We convert them to standard Python integers first
    c_lib.process_point(int(x_int), int(y_int), int(z_int))

except (Exception) as e:
    print(f"An error occurred during C interaction: {e}")
    exit()


# --- Part 3: Generate the 3D Plot ---

def plane1(x, y): return (5 - 5*x + y) / 4
def plane2(x, y): return (2 - 2*x - 3*y) / 5
def plane3(x, y): return (-1 - 5*x + 2*y) / 6

x_grid, y_grid = np.meshgrid(np.linspace(-2, 8, 20), np.linspace(-2, 8, 20))
z1 = plane1(x_grid, y_grid)
z2 = plane2(x_grid, y_grid)
z3 = plane3(x_grid, y_grid)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_grid, y_grid, z1, alpha=0.6, color='red')
ax.plot_surface(x_grid, y_grid, z2, alpha=0.6, color='green')
ax.plot_surface(x_grid, y_grid, z3, alpha=0.6, color='blue')
ax.scatter(x_int, y_int, z_int, color='black', s=150, ec='white', zorder=10)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Planes Intersecting at a Point Calculated by Python')

legend_elements = [
    Line2D([0], [0], color='red', lw=4, label='5x - y + 4z = 5'),
    Line2D([0], [0], color='green', lw=4, label='2x + 3y + 5z = 2'),
    Line2D([0], [0], color='blue', lw=4, label='5x - 2y + 6z = -1'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=10, label=f'Intersection: ({x_int:.0f}, {y_int:.0f}, {z_int:.0f})')
]
ax.legend(handles=legend_elements)

plt.show()
