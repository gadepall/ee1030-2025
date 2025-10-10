import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define data structures to match C code ---

# Define the Point3D structure for ctypes
class Point3D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Define constants for the UnknownCoord enum
UNKNOWN_X = 0
UNKNOWN_Y = 1
UNKNOWN_Z = 2

# --- 2. Load the shared library and define the function signature ---

# Load the compiled shared library
c_lib = ctypes.CDLL('./1.so')

# Get a handle to the C function
solve_coplanar_coord = c_lib.solve_coplanar_coord

# Define the function's argument types and return type for type safety
solve_coplanar_coord.argtypes = [Point3D, Point3D, Point3D, Point3D, 
                                ctypes.c_int, ctypes.c_int]
solve_coplanar_coord.restype = ctypes.c_double

# --- 3. Prepare data and call the C function ---

# Create instances of the Point3D structure for our points
A = Point3D(3, -2, -1)
B = Point3D(2, 3, -4)
C = Point3D(-1, 1, 2)
# Point D with a placeholder (0) for the unknown lambda (z-coordinate)
D = Point3D(4, 5, 0) 

# Call the C function from Python!
# We ask it to solve for the Z coordinate (2) of the 4th point (index 3)
lambda_val = solve_coplanar_coord(A, B, C, D, 3, UNKNOWN_Z)

print(f"The value of lambda calculated by the C function is: {lambda_val:.17f}")

# --- 4. Plot the points using Matplotlib ---

# Update the z-coordinate of point D with the calculated value
D.z = lambda_val

# Convert ctypes structures to NumPy arrays for easy plotting
points = {
    'A': np.array([A.x, A.y, A.z]),
    'B': np.array([B.x, B.y, B.z]),
    'C': np.array([C.x, C.y, C.z]),
    'D': np.array([D.x, D.y, D.z])
}

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot and label each point
for name, p in points.items():
    ax.scatter(p[0], p[1], p[2], color='blue', s=60)
    label = f' {name} ({p[0]:.2f}, {p[1]:.2f}, {p[2]:.2f})'
    ax.text(p[0], p[1], p[2], label, size=11, color='k')

# Formatting the plot
ax.set_xlabel('X-axis', fontweight='bold')
ax.set_ylabel('Y-axis', fontweight='bold')
ax.set_zlabel('Z-axis', fontweight='bold')
ax.set_title('3D Plot of Points Calculated via C Function', fontsize=16)
ax.grid(True)
plt.savefig('1.png')
plt.show()