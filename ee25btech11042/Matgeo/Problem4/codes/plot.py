import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Load the shared library ---
lib = ctypes.CDLL('./2.10.70.so')

# --- Step 2: Define the C function signature using NumPy-aware pointers ---
calculate_points = lib.calculate_points_from_arrays

# Define the argument types. 'ndpointer' creates a ctypes-compatible type for NumPy arrays.
calculate_points.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'), # input_A
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'), # input_B
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'), # input_C
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS')  # output_points
]
# The function has a 'void' return type in C
calculate_points.restype = None

# --- Step 3: Prepare NumPy arrays and call the C function ---
# Define the vertices of the triangle as NumPy arrays
A = np.array([0.0, 0.0], dtype=np.double)
B = np.array([6.0, 1.0], dtype=np.double)
C = np.array([2.0, 5.0], dtype=np.double)

# Create an empty NumPy array for the C function to fill
# It needs to have space for 6 points (6 * 2 = 12 doubles)
output_data = np.zeros(12, dtype=np.double)

# Call the C function. NumPy arrays are passed directly.
calculate_points(A, B, C, output_data)

# --- Step 4: Reshape the output and plot ---
# Reshape the flat output array into a 6x2 array (6 points, 2 coords each)
points_array = output_data.reshape(6, 2)

point_names = ['A', 'B', 'C', 'D', 'E', 'P']
points = {name: coord for name, coord in zip(point_names, points_array)}

print("Coordinates calculated by C library and loaded into NumPy:")
for name, coords in points.items():
    print(f"  Point {name}: ({coords[0]:.4f}, {coords[1]:.4f})")

# Plotting logic remains the same
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle=':', alpha=0.7)

triangle = plt.Polygon(points_array[:3], edgecolor='darkblue', facecolor='lightblue', alpha=0.4, linewidth=2, label='Triangle ABC')
ax.add_patch(triangle)

ax.plot([points['A'][0], points['D'][0]], [points['A'][1], points['D'][1]], 'r--', label='Line AD')
ax.plot([points['B'][0], points['E'][0]], [points['B'][1], points['E'][1]], 'g--', label='Line BE')
            
for name, coords in points.items():
    color = 'red' if name == 'P' else 'black'
    size = 12 if name == 'P' else 8
    ax.plot(coords[0], coords[1], 'o', markersize=size, color=color, label=f'Point {name}')
    ax.text(coords[0] + 0.15, coords[1] + 0.15, name, fontsize=14, fontweight='bold', color=color)

ax.set_title('Plot from C Library using NumPy and ctypes', fontsize=16)
ax.legend(loc="upper left")

plt.figure()
plt.savefig('numpy_ctypes_plot.png')

plt.show()
