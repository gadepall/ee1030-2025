import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import ctypes
import os

# Load the shared library
lib = ctypes.CDLL('./code.so')

# Define C types matching the exact structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

class Solutions(ctypes.Structure):
    _fields_ = [("count", ctypes.c_int),
                ("solution1", ctypes.c_double),
                ("solution2", ctypes.c_double)]

# Set up function prototypes exactly as in C
lib.solveForA.argtypes = [Point, ctypes.c_double, Point]
lib.solveForA.restype = Solutions

lib.getValidA.argtypes = []
lib.getValidA.restype = ctypes.c_double

# Get the value of a from C library using the exact function
a_value = lib.getValidA()
print(f"Value of a from C library: {a_value}")

# Define points
A = np.array([2, 9])
B = np.array([a_value, 5])
C = np.array([5, 5])

print(f"Coordinates:")
print(f"A({A[0]}, {A[1]})")
print(f"B({B[0]}, {B[1]})")
print(f"C({C[0]}, {C[1]})")

# Function to generate line points
def line_gen(P, Q):
    return np.column_stack((P, Q))

# Calculate triangle properties
c = LA.norm(A - B)
a = LA.norm(B - C)
b = LA.norm(C - A)
print(f"\nSide lengths:")
print(f"AB = {c:.2f}")
print(f"BC = {a:.2f}")
print(f"CA = {b:.2f}")

# Calculate area (since it's right-angled at B)
area = 0.5 * a * c
print(f"\nArea of triangle ABC: {area:.2f}")

# Generate lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Plotting
plt.figure(figsize=(10, 8))
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$', linewidth=3, color='blue')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$', linewidth=3, color='green')
plt.plot(x_CA[0,:], x_CA[1,:], label='$CA$', linewidth=3, color='red')

# Labeling the coordinates
tri_coords = np.column_stack((A, B, C))
plt.scatter(tri_coords[0,:], tri_coords[1,:], color='black', s=150, zorder=5)

vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, 
                 (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points",
                 xytext=(0,15),
                 ha='center',
                 fontsize=14,
                 fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.title(f'Right-Angled Triangle ABC at B\nB = ({B[0]:.1f}, {B[1]:.1f}), Area = {area:.2f}', fontsize=16)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.axis('equal')

# Set appropriate limits with some padding
plt.xlim(min(tri_coords[0,:]) - 1, max(tri_coords[0,:]) + 1)
plt.ylim(min(tri_coords[1,:]) - 1, max(tri_coords[1,:]) + 1)

# Add right angle marker at B
angle_x = B[0] + 0.5
angle_y = B[1] + 0.5
plt.plot([B[0], angle_x], [B[1], B[1]], 'k--', alpha=0.5)
plt.plot([B[0], B[0]], [B[1], angle_y], 'k--', alpha=0.5)
plt.text(B[0] + 0.3, B[1] + 0.3, '90°', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('../figs/fig1.png')
plt.show()
