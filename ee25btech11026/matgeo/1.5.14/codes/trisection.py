import ctypes
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./libintdiv_formula.so')
lib.find_section_point.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                   ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                   ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.find_section_point.restype = None

def find_section_point(x1, y1, x2, y2, m, n):
    x = ctypes.c_double()
    y = ctypes.c_double()
    lib.find_section_point(x1, y1, x2, y2, m, n, ctypes.byref(x), ctypes.byref(y))
    return (x.value, y.value)

# Given points
A = (-2,0)
B = (0,8)

# Find P such that AP:PB=1:2
P = find_section_point(A[0], A[1], B[0], B[1], 1, 2)
# Find Q such that AQ:QB=2:1
Q = find_section_point(A[0], A[1], B[0], B[1], 2, 1)

# Format results
P_formatted = (round(P[0], 2), round(P[1], 2))
Q_formatted = (round(Q[0], 2), round(Q[1], 2))

print(f"P: {P_formatted}")
print(f"Q: {Q_formatted}")

# Plotting
plt.figure(figsize=(8, 8))

# Line AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'ro-', label='AB')

# Points P and Q
plt.plot(*P_formatted, 'go', label='P', markersize=8)   # green
plt.plot(*Q_formatted, 'bo', label='Q', markersize=8)   # blue

# Labels
plt.text(A[0]+0.1, A[1], 'A', fontsize=12, ha='right')
plt.text(B[0]+0.1, B[1], 'B', fontsize=12, ha='right')
plt.text(*P_formatted, f'P {P_formatted}', fontsize=12, ha='right', color='green')
plt.text(*Q_formatted, f'Q {Q_formatted}', fontsize=12, ha='left', color='blue')

mp.use("TkAgg")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trisection of line AB by points P and Q')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Save before show
plt.savefig("/home/user/Matrix/Matgeo_assignments/1.5.14/figs/Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()

