import ctypes
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

lib=ctypes.CDLL("./lib_dis_matrix.so")

lib.displacement_matrix.argtypes=(np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),ctypes.c_double)

def shear_matrix(gamma: float) -> np.ndarray:
    mat = np.zeros(4, dtype=np.float64)  # flattened 2x2
    lib.displacement_matrix(mat, gamma)
    return mat.reshape((2, 2))

# Example usage
gamma = 0.5
A= shear_matrix(gamma)
B=sp.Matrix(A)
print("Displacement matrix:\n")
sp.pprint(B)

# Define rectangle corners (counter-clockwise)
rect = np.array([[0, 0],
                 [2, 0],
                 [2, 1],
                 [0, 1],
                 [0, 0]])  # closed loop

# Apply shear transformation
deformed = rect @ B.T

# Plot
plt.figure(figsize=(8, 8))
plt.plot(rect[:, 0], rect[:, 1], 'b-', label='Original Rectangle')
plt.plot(deformed[:, 0], deformed[:, 1], 'r--', label='Sheared Parallelogram')
plt.fill(rect[:, 0], rect[:, 1], 'b', alpha=0.2)
plt.fill(deformed[:, 0], deformed[:, 1], 'r', alpha=0.2)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc="upper right")
plt.title(f"Simple Shear Deformation (gamma = {gamma})")
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/12.456/figs/Figure_1.png")
plt.show()


