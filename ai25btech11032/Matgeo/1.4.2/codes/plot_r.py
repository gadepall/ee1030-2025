import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library (Linux name shown here)
lib = ctypes.CDLL("./librpoint.so")

# Tell ctypes the C function signature
lib.point_on_segment2d.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # P
    ctypes.POINTER(ctypes.c_double),  # Q
    ctypes.c_double,                  # lambda
    ctypes.POINTER(ctypes.c_double)   # R
]
lib.point_on_segment2d.restype = None

# Data
P = np.array([1.0, 3.0], dtype=np.float64)
Q = np.array([2.0, 5.0], dtype=np.float64)
lam = 3.0/5.0
R = np.zeros(2, dtype=np.float64)

# Call C
lib.point_on_segment2d(
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    Q.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    lam,
    R.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

print("R from C:", tuple(R))  # Expect (1.6, 4.2)

# Plot
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'k--', label="PQ")
plt.scatter(*P, color='red', label="P")
plt.scatter(*Q, color='blue', label="Q")
plt.scatter(*R, color='green', label="R")
plt.legend()
plt.title("R = P + (3/5)(Q − P)")

# Save first, then show
plt.savefig("/sdcard/ee1030-2025/ai25btech11032/Matgeo/1.4.2/figs/PQ_R_plotnew.png", dpi=300)
plt.show()
