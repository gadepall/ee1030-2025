import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, c_double, POINTER

# Load the shared library
lib = CDLL('./libtriangle.so')

# Setup argument types for C function
lib.find_third_vertex.argtypes = [POINTER(c_double), POINTER(c_double)]

def get_third_vertex():
    x = c_double()
    y = c_double()
    lib.find_third_vertex(x, y)
    return x.value, y.value

# Given vertices
A = np.array([-4, 3])
B = np.array([4, 3])
C = np.array(get_third_vertex())
Origin = np.array([0, 0])

# Plot the triangle edges
plt.figure(figsize=(7, 7))
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label='AB')
plt.plot([B[0], C[0]], [B[1], C[1]], 'g-', label='BC')
plt.plot([C[0], A[0]], [C[1], A[1]], 'r-', label='CA')

# Mark and label points
plt.scatter(*A, color='blue')
plt.text(A[0], A[1]+0.3, "A (-4,3)", color='blue')

plt.scatter(*B, color='green')
plt.text(B[0], B[1]+0.3, "B (4,3)", color='green')

plt.scatter(*C, color='red')
plt.text(C[0], C[1]-0.5, f"C ({C[0]:.2f}, {C[1]:.2f})", color='red')

plt.scatter(*Origin, color='black', marker='x')
plt.text(Origin[0]+0.2, Origin[1], 'Origin (0,0)', color='black')

plt.title("Equilateral Triangle with Origin Inside")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.tight_layout()
plt.show()

