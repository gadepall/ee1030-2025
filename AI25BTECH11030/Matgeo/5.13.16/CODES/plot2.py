import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('./matfun.so')

arr_type = ctypes.c_double * 2
A = arr_type(2, -6)
B = arr_type(5, 2)
C = arr_type(-2, 2)
O = arr_type()

# Set arg types
lib.compute_orthocentre.argtypes = [arr_type, arr_type, arr_type, arr_type]
lib.line_equation.argtypes = [arr_type, arr_type, arr_type, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.solve_2x2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, arr_type]

# Call orthocentre computation
lib.compute_orthocentre(A, B, C, O)
print("Orthocentre:", list(O))

# Arrays to hold line coefficients
a1, b1, c1 = ctypes.c_double(), ctypes.c_double(), ctypes.c_double()
a2, b2, c2 = ctypes.c_double(), ctypes.c_double(), ctypes.c_double()
a3, b3, c3 = ctypes.c_double(), ctypes.c_double(), ctypes.c_double()

# Compute altitude lines via C functions for all three vertices
lib.line_equation(A, B, C, ctypes.byref(a1), ctypes.byref(b1), ctypes.byref(c1)) # Altitude from A
lib.line_equation(B, A, C, ctypes.byref(a2), ctypes.byref(b2), ctypes.byref(c2)) # Altitude from B
lib.line_equation(C, A, B, ctypes.byref(a3), ctypes.byref(b3), ctypes.byref(c3)) # Altitude from C

# Convert points to numpy for plotting
A_np = np.array([2, -6])
B_np = np.array([5, 2])
C_np = np.array([-2, 2])
O_np = np.array([O[0], O[1]])

fig, ax = plt.subplots(figsize=(6,6))
ax.plot([A_np[0], B_np[0], C_np[0], A_np[0]], [A_np[1], B_np[1], C_np[1], A_np[1]], 'bo-', label='Triangle')

def plot_line(a, b, c, ax, color, label):
    if abs(b) > 1e-8:
        x = np.linspace(-10, 20, 300)
        y = (c - a*x)/b
    else:
        x = np.full(300, c/a)
        y = np.linspace(-10, 20, 300)
    ax.plot(x, y, color=color, linestyle='--', label=label)

plot_line(a1.value, b1.value, c1.value, ax, 'r', 'Altitude from A')
plot_line(a2.value, b2.value, c2.value, ax, 'g', 'Altitude from B')
plot_line(a3.value, b3.value, c3.value, ax, 'b', 'Altitude from C')

ax.plot(O_np[0], O_np[1], 'ro', label='Orthocentre')

ax.legend()
ax.grid(True)
ax.set_title('Triangle, Altitudes, and Orthocentre (using .so functions)')
plt.show()

