import ctypes
import matplotlib as mp
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('./libsection_formula.so')
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
A = (-2, 2)
B = (2, -4)

# We want P such that AP:PB = 3:4  (since AP = 3/7 AB)
P = find_section_point(A[0], A[1], B[0], B[1], 3, 4)

# Format result
P_formatted = (round(P[0], 2), round(P[1], 2))
print(f"P: {P_formatted}")

# Plotting
plt.figure(figsize=(8, 8))

# Line AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'ro-', label='AB')

# Point P
plt.plot(*P_formatted, 'go', label='P', markersize=8)

# Labels
plt.text(A[0]-0.2, A[1]+0.2, 'A', fontsize=12, ha='right')
plt.text(B[0]+0.2, B[1]-0.2, 'B', fontsize=12, ha='left')
plt.text(*P_formatted, f'P {P_formatted}', fontsize=12, ha='left', color='green')

mp.use("TkAgg")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Point P dividing AB in ratio 3:4')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Save before show
plt.savefig("Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()
