import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file (compiled from your C code)
lib = ctypes.CDLL('./lib1.so')  # change name if your .so file is different

# Define argument and return types for the C function
lib.find_a.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.find_a.restype = ctypes.c_double

# Given data
x1, y1 = -6, 5
x2, y2 = -2, 3
given_y = 4

# Call the C function
a_value = lib.find_a(x1, y1, x2, y2, given_y)
print(f"Value of a: {a_value}")

# Midpoint coordinates from a
mid_x = a_value / 4
mid_y = given_y

# Create numpy arrays for plotting
A = np.array([x1, y1])
B = np.array([x2, y2])
M = np.array([mid_x, mid_y])

# Generate line between A and B
line_AB = np.column_stack((A, B))

# Plotting
plt.plot([A[0], B[0]], [A[1], B[1]], label='$AB$')
plt.scatter([A[0], B[0], M[0]], [A[1], B[1], M[1]], color=['red', 'blue', 'green'])

# Annotate points
labels = ['A', 'B', 'Midpoint']
coords = [A, B, M]
for label, coord in zip(labels, coords):
    plt.annotate(f'{label}\n({coord[0]:.2f}, {coord[1]:.2f})',
                 (coord[0], coord[1]),
                 textcoords="offset points",
                 xytext=(10, -10),
                 ha='center')

plt.legend()
plt.grid(True)
plt.axis('equal')
plt.savefig('1.png')
plt.show()