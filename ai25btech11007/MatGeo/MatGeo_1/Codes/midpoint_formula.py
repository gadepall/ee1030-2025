import ctypes
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('./libintdiv_formula.so')
lib.find_section_point.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                   ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                   ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.find_section_point.restype = None

# Section point finder
def find_section_point(x1, y1, x2, y2, m, n):
    x = ctypes.c_double()
    y = ctypes.c_double()
    lib.find_section_point(x1, y1, x2, y2, m, n, ctypes.byref(x), ctypes.byref(y))
    return (x.value, y.value)

# -----------------------------------------------------------
# Given parallelogram vertices
# A(1,2), B(4,y), C(x,6), D(3,5)
# Property: diagonals bisect each other
# -----------------------------------------------------------

# Midpoint of AC
M_AC = find_section_point(1, 2, 6, 6, 1, 1)   # A(1,2), C(x=6,6)
# Midpoint of BD
M_BD = find_section_point(4, 3, 3, 5, 1, 1)   # B(4,y=3), D(3,5)

print(f"Midpoint of AC: {M_AC}")
print(f"Midpoint of BD: {M_BD}")

# Final solved values
x = 6
y = 3
A = (1, 2)
B = (4, y)
C = (x, 6)
D = (3, 5)

# -----------------------------------------------------------
# Plotting parallelogram
# -----------------------------------------------------------
plt.figure(figsize=(8, 8))

# Draw parallelogram edges
X = [A[0], B[0], C[0], D[0], A[0]]
Y = [A[1], B[1], C[1], D[1], A[1]]
plt.plot(X, Y, 'ro-', label='Parallelogram')

# Draw diagonals
plt.plot([A[0], C[0]], [A[1], C[1]], 'g--', label='Diagonal AC')
plt.plot([B[0], D[0]], [B[1], D[1]], 'b--', label='Diagonal BD')

# Labels
plt.text(A[0]-0.2, A[1]-0.2, 'A(1,2)', fontsize=12)
plt.text(B[0]+0.2, B[1], f'B(4,{y})', fontsize=12)
plt.text(C[0]+0.2, C[1], f'C({x},6)', fontsize=12)
plt.text(D[0]-0.4, D[1], 'D(3,5)', fontsize=12)

# Midpoints
plt.plot(M_AC[0], M_AC[1], 'ks', label='Midpoint of AC')
plt.plot(M_BD[0], M_BD[1], 'ms', label='Midpoint of BD')

# Style
mp.use("TkAgg")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parallelogram with Diagonals Bisecting Each Other')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Save figure
plt.savefig("/home/user/Matrix/Matgeo_assignments/1.5.16/figs/Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()
