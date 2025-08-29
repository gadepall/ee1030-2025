import ctypes
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

# Load the shared library (C function for midpoint check)
lib = ctypes.CDLL('./libintdiv_formula.so')
lib.find_midpoint.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                              ctypes.c_double,
                              ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.find_midpoint.restype = None

def find_midpoint(x1, y1, x2, y2):
    """Calls C function to compute midpoint of (x1,y1) and (x2,y2)."""
    x = ctypes.c_double()
    y = ctypes.c_double()
    lib.find_midpoint(x1, y1, x2, y2, ctypes.byref(x), ctypes.byref(y))
    return (x.value, y.value)

# Given vertices of parallelogram
A = (1, 2)
B = (4, None)   # y unknown
C = (None, 6)   # x unknown
D = (3, 5)

# Midpoint of AC and BD must be equal
# Midpoint(AC) = ((1+x)/2, (2+6)/2)
# Midpoint(BD) = ((4+3)/2, (y+5)/2)

# Solve equations manually (since x and y are unknown)
x = 6
y = 3

# Substitute solved values
B = (4, y)
C = (x, 6)

# Find midpoints using C function
mid_AC = find_midpoint(A[0], A[1], C[0], C[1])
mid_BD = find_midpoint(B[0], B[1], D[0], D[1])

print(f"Midpoint of AC: {mid_AC}")
print(f"Midpoint of BD: {mid_BD}")
print(f"Solution: x = {x}, y = {y}")

# --- Plotting the parallelogram ---
plt.figure(figsize=(8, 8))

# Plot parallelogram
X = [A[0], B[0], C[0], D[0], A[0]]
Y = [A[1], B[1], C[1], D[1], A[1]]
plt.plot(X, Y, 'ro-', label='Parallelogram')

# Plot diagonals
plt.plot([A[0], C[0]], [A[1], C[1]], 'g--', label='Diagonal AC')
plt.plot([B[0], D[0]], [B[1], D[1]], 'b--', label='Diagonal BD')

# Mark points
for point, name in zip([A, B, C, D], ['A', 'B', 'C', 'D']):
    plt.plot(point[0], point[1], 'ko')
    plt.text(point[0]+0.1, point[1], f'{name}{point}', fontsize=12)

# Mark midpoints
plt.plot(mid_AC[0], mid_AC[1], 'ms', label=f'Midpoint {mid_AC}')
plt.plot(mid_BD[0], mid_BD[1], 'cs', label=f'Midpoint {mid_BD}')

mp.use("TkAgg")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parallelogram with Diagonals Bisecting Each Other')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Save before show
plt.savefig("/home/user/Matrix/Matgeo_assignments/1.5.15/figs/Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()
