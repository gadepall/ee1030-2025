import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes

# --- 1. Load C Library and Define Interfaces ---
lib = ctypes.CDLL("./12.263.so")

lib.solve_lu.argtypes = [
    ctypes.c_double * 9,  # A matrix
    ctypes.c_double * 3,  # b vector
    ctypes.c_double * 3,  # z_out vector
    ctypes.c_double * 3   # x_out vector
]

# --- 2. Define Inputs and Call C Function ---

# Define the matrix A and vector b from the problem
A_list = [1.0, 1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 3.0, 2.0]
b_list = [1.0, 1.0, 1.0]

# Convert to C-style arrays
A_c = (ctypes.c_double * 9)(*A_list)
b_c = (ctypes.c_double * 3)(*b_list)

# Create empty C-style arrays to hold the results
z_solution_c = (ctypes.c_double * 3)()
x_solution_c = (ctypes.c_double * 3)()

# Call the C function to perform all calculations
lib.solve_lu(A_c, b_c, z_solution_c, x_solution_c)

# Convert C array results back to NumPy arrays for use in Python
z_solution = np.array(z_solution_c)
x_solution = np.array(x_solution_c)

print("--- Results from C Function ---")
print(f"Intermediate vector z: {z_solution}")
print(f"Final solution vector x: {x_solution}")
print("-----------------------------\n")

# --- 3. Prepare for 3D Plotting ---

# Create a meshgrid for the surface plots
x_range = np.arange(-5, 5, 0.25)
y_range = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x_range, y_range)

# Equations of the planes, solved for Z
Z1 = 1 - X - Y
Z2 = (1 - 2*X - Y) / 2
Z3 = (1 - X - 3*Y) / 2

# --- 4. Create the Plot ---

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the three planes
ax.plot_surface(X, Y, Z1, alpha=0.5)
ax.plot_surface(X, Y, Z2, alpha=0.5, color='green')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='orange')

# Plot the intersection point found by the C function
ax.scatter(x_solution[0], x_solution[1], x_solution[2], color='red', s=100, zorder=10, label=f'Intersection: ({x_solution[0]:.0f}, {x_solution[1]:.0f}, {x_solution[2]:.0f})')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Intersection of Three Planes')
ax.legend()

plt.show()
