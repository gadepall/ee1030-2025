import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./vector.so")   # use "vec.dll" on Windows

# Define argument & return types
lib.compute.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    ctypes.POINTER(ctypes.c_double),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS")
]

# Example vectors
a = np.array([1.0, 0.0], dtype=np.double)
b = np.array([0.6, 0.8], dtype=np.double)

M = ctypes.c_double()
u = np.zeros(2, dtype=np.double)

# Call C function
lib.compute(a, b, ctypes.byref(M), u)

print("From C library:")
print("M =", M.value)
print("u =", u)

# Plot in same style as attachment
O = np.array([0.0, 0.0])
P = u * M.value

plt.plot([O[0], P[0]], [O[1], P[1]], 'b-', label="Vector OP")
plt.scatter(*O, color="red", s=100, label="O(0,0)")
plt.scatter(*P, color="green", s=100, label=f"P({P[0]:.2f},{P[1]:.2f})")
plt.scatter(*u, color="purple", marker="*", s=200, label=f"u({u[0]:.2f},{u[1]:.2f})")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.title("Figure")
plt.grid(True)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/2.10.56/figs/figure1.png")
plt.show()
