import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib_geometry = ctypes.CDLL("./code2.so")

# Define argument and return types for findMidpoint
lib_geometry.findMidpoint.argtypes = [
    ctypes.c_double,  # x1
    ctypes.c_double,  # y1
    ctypes.c_double,  # x2
    ctypes.c_double,  # y2
    ctypes.POINTER(ctypes.c_double), # mid_x
    ctypes.POINTER(ctypes.c_double)  # mid_y
]
lib_geometry.findMidpoint.restype = None

# Define argument and return types for calculateDistance
lib_geometry.calculateDistance.argtypes = [
    ctypes.c_double,  # x1
    ctypes.c_double,  # y1
    ctypes.c_double,  # x2
    ctypes.c_double   # y2
]
lib_geometry.calculateDistance.restype = ctypes.c_double

# Vertices of the triangle
A_x, A_y = 5.0, -6.0
B_x, B_y = 6.0, 4.0
C_x, C_y = 0.0, 0.0

# Create ctypes doubles to hold the midpoint D coordinates
D_x_result = ctypes.c_double()
D_y_result = ctypes.c_double()

# Call the C function to find the midpoint D of BC
lib_geometry.findMidpoint(
    B_x, B_y,
    C_x, C_y,
    ctypes.byref(D_x_result),
    ctypes.byref(D_y_result)
)

D_x = D_x_result.value
D_y = D_y_result.value

print(f"Coordinates of D (midpoint of BC): ({D_x:.2f}, {D_y:.2f})")

# Call the C function to find the length of AD
length_AD = lib_geometry.calculateDistance(
    A_x, A_y,
    D_x, D_y
)

print(f"The length of the median AD is: {length_AD:.2f}")

# Plotting the triangle and median
plt.figure(figsize=(10, 8))

# Plot vertices
plt.scatter([A_x, B_x, C_x], [A_y, B_y, C_y], color='blue', s=100, zorder=5)
plt.annotate(f'A({A_x},{A_y})', (A_x, A_y), textcoords="offset points", xytext=(5,5), ha='left')
plt.annotate(f'B({B_x},{B_y})', (B_x, B_y), textcoords="offset points", xytext=(5,5), ha='left')
plt.annotate(f'C({C_x},{C_y})', (C_x, C_y), textcoords="offset points", xytext=(5,5), ha='left')

# Plot point D
plt.scatter(D_x, D_y, color='red', s=100, zorder=5, label=f'D({D_x:.1f},{D_y:.1f})')
plt.annotate(f'D({D_x:.1f},{D_y:.1f})', (D_x, D_y), textcoords="offset points", xytext=(5,5), ha='left')


# Plot triangle sides
plt.plot([A_x, B_x], [A_y, B_y], 'k-')
plt.plot([B_x, C_x], [B_y, C_y], 'k-')
plt.plot([C_x, A_x], [C_y, A_y], 'k-', label='Triangle ABC')

# Plot median AD
plt.plot([A_x, D_x], [A_y, D_y], 'g--', label=f'Median AD (Length: {length_AD:.2f})')

plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle ABC and Median AD')
plt.grid(True)
plt.legend()
plt.savefig("fig1.png")
plt.show()
