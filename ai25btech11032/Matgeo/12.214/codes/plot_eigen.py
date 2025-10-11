import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./eigen.so")

# Define arg/return types
lib.eigenvalues.argtypes = [ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double)]
lib.eigenvalues.restype = None

lib.eigenvector.argtypes = [ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.c_double,
                            ctypes.POINTER(ctypes.c_double)]
lib.eigenvector.restype = None

# Example matrix A = [[3,4],[4,-3]]
a, b, c, d = 3.0, 4.0, 4.0, -3.0

eig1 = ctypes.c_double()
eig2 = ctypes.c_double()

# Get eigenvalues
lib.eigenvalues(a, b, c, d, ctypes.byref(eig1), ctypes.byref(eig2))
print("Eigenvalues:", eig1.value, eig2.value)

# Get eigenvectors
v1 = (ctypes.c_double * 2)()
v2 = (ctypes.c_double * 2)()

lib.eigenvector(a, b, c, d, eig1.value, v1)
lib.eigenvector(a, b, c, d, eig2.value, v2)

vec1 = np.array([v1[0], v1[1]])
vec2 = np.array([v2[0], v2[1]])

print("Eigenvector for eig1:", vec1)
print("Eigenvector for eig2:", vec2)

# ---- Plot ----
plt.figure(figsize=(5,5))
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

plt.quiver(0, 0, vec1[0], vec1[1], angles='xy', scale_units='xy', scale=1,
           color="red", label=f"eig1={eig1.value:.2f}")
plt.quiver(0, 0, vec2[0], vec2[1], angles='xy', scale_units='xy', scale=1,
           color="blue", label=f"eig2={eig2.value:.2f}")

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True)
plt.legend()
plt.title("Eigenvectors of A = [[3,4],[4,-3]]")

# Save figure
plt.savefig("eigenvectors.png", dpi=300)

# Show figure
plt.show()

