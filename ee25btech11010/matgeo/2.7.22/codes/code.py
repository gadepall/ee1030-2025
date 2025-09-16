import ctypes
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Load C shared library
# ==============================
lib = ctypes.CDLL("./code.so")

# Define function signature
lib.triangle_area.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double]
lib.triangle_area.restype = ctypes.c_double

# Triangle vertices
A = (5.0, 0.0)
B = (8.0, 0.0)
C = (8.0, 4.0)

# Compute area using the C function
area = lib.triangle_area(A[0], A[1], B[0], B[1], C[0], C[1])
print(f"Area of the triangle (from C): {area:.2f} sq.units")

# ==============================
# Plotting the triangle
# ==============================
x_coords = [A[0], B[0], C[0], A[0]]  # close the triangle
y_coords = [A[1], B[1], C[1], A[1]]

plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'bo-', label='Triangle')
plt.fill(x_coords, y_coords, 'skyblue', alpha=0.3)

# Label the points
plt.text(A[0], A[1]-0.3, f'A{A}', ha='center')
plt.text(B[0], B[1]-0.3, f'B{B}', ha='center')
plt.text(C[0]+0.2, C[1], f'C{C}', ha='center')

# Add grid, axis, and title
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(f'Triangle with vertices A{A}, B{B}, C{C}\nArea = {area:.2f} sq. units')
plt.axis('equal')
plt.legend()
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/2.7.22/figs/q4.png")
plt.show()
