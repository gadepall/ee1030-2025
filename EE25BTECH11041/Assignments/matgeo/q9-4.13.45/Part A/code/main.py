import ctypes
from ctypes import Structure, c_double
import matplotlib.pyplot as plt

# Define Point struct
class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

# Load shared object
lib = ctypes.CDLL("./libtriangle.so")
lib.third_vertex.restype = Point
lib.third_vertex.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# Given vertices and orthocenter
A_x, A_y = 5, -1
B_x, B_y = 2, -3
H_x, H_y = 0, 0

# Call C function
C = lib.third_vertex(A_x, A_y, B_x, B_y, H_x, H_y)
print(f"Third vertex: ({C.x:.2f}, {C.y:.2f})")

# Plot triangle
x_coords = [A_x, B_x, C.x, A_x]
y_coords = [A_y, B_y, C.y, A_y]

plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'b-o', label='Triangle')
plt.plot(H_x, H_y, 'r*', markersize=12, label='Orthocenter')
plt.text(A_x, A_y, 'A', fontsize=12, ha='right')
plt.text(B_x, B_y, 'B', fontsize=12, ha='right')
plt.text(C.x, C.y, 'C', fontsize=12, ha='right')
plt.text(H_x, H_y, 'H', fontsize=12, ha='right')
plt.grid(True)
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle with Orthocenter')
plt.show()

