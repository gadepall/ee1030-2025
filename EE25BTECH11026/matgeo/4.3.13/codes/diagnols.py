import ctypes
import numpy as np
import matplotlib as mp
mp.use("TkAgg")
import matplotlib.pyplot as plt

# Load C shared library
lib = ctypes.CDLL("./libdiagonals.so")

# Define argument types for the function
lib.diagonal_equations.argtypes = [
    (ctypes.c_double * 2) * 4,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

# Define square vertices
vertices = [(0.0,0.0), (1.0,0.0), (1.0,1.0), (0.0,1.0)]
vert_array = ((ctypes.c_double*2)*4)(*[(ctypes.c_double*2)(*v) for v in vertices])

# Output containers
n1 = (ctypes.c_double*2)()
c1 = ctypes.c_double()
n2 = (ctypes.c_double*2)()
c2 = ctypes.c_double()

# Call C function
lib.diagonal_equations(vert_array, n1, ctypes.byref(c1), n2, ctypes.byref(c2))

n1 = np.array([n1[0], n1[1]])
n2 = np.array([n2[0], n2[1]])

# Convert to Cartesian equation: ax + by + d = 0
def cartesian_eq(n, c):
    a, b = n
    d = -c
    eq = []
    if a != 0:
        eq.append(f"{a}x")
    if b != 0:
        sign = "+" if b > 0 and eq else ""
        eq.append(f"{sign}{b}y")
    if d != 0:
        sign = "+" if d > 0 and eq else ""
        eq.append(f"{sign}{d}")
    return " ".join(eq) + " = 0"

eq1 = cartesian_eq(n1, c1.value)
eq2 = cartesian_eq(n2, c2.value)

print("Diagonal AC (normal form):", f"[{n1[0]} {n1[1]}] · [x y]^T = {c1.value}")
print("Diagonal BD (normal form):", f"[{n2[0]} {n2[1]}] · [x y]^T = {c2.value}")

# ---- PLOT ----
A, B, C, D = vertices
square_x = [A[0], B[0], C[0], D[0], A[0]]
square_y = [A[1], B[1], C[1], D[1], A[1]]

plt.plot(square_x, square_y, 'b-', label='Square')

# Plot diagonals
plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', label=eq1)
plt.plot([B[0], D[0]], [B[1], D[1]], 'g--', label=eq2)

plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc="upper right")
plt.grid(True)
plt.savefig("/home/user/Matrix/Matgeo_assignments/4.3.13/figs/Figure_1.png")
plt.show()

