import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./vectors.so")   # use "vectors.dll" on Windows

# Define argument and return types
lib.compute_vectors.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
]
lib.compute_vectors.restype = None

# Input vectors
B = np.array([0.5, np.sqrt(3)/2, 0.0], dtype=np.float64)
C = np.array([0.5, -np.sqrt(3)/2, 0.0], dtype=np.float64)

# Output arrays
A1 = np.zeros(3, dtype=np.float64)
A2 = np.zeros(3, dtype=np.float64)

# Call C function
lib.compute_vectors(B, C, A1, A2)

# --- Plot ---
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

vectors = {"B": B, "C": C, "A1": A1, "A2": A2}
colors = {"B": "r", "C": "g", "A1": "b", "A2": "m"}

for name, vec in vectors.items():
    ax.quiver(0,0,0, vec[0], vec[1], vec[2], color=colors[name], label=name)
    ax.text(vec[0], vec[1], vec[2], f"{name}{tuple(vec.round(2))}")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Vectors from C + Python (ctypes)")
ax.legend()
plt.show()