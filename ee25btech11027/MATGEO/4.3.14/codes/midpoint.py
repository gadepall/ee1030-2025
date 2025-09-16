import ctypes
import matplotlib.pyplot as plt

# Load compiled C library
lib = ctypes.CDLL("./midpoint.so")

# Define return type and argument types
lib.get_points.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
                           ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]

# Prepare variables
Px, Py, Qx, Qy = ctypes.c_int(), ctypes.c_int(), ctypes.c_int(), ctypes.c_int()

# Call C function
lib.get_points(ctypes.byref(Px), ctypes.byref(Py), ctypes.byref(Qx), ctypes.byref(Qy))

# Extract results
P = (Px.value, Py.value)
Q = (Qx.value, Qy.value)
M = (2, 5)  # midpoint given

# --- Plotting ---
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'b-', label="Line PQ")

# Plot P, Q, M
plt.scatter(*P, color="red", s=100, label=f"P{P}")
plt.scatter(*Q, color="green", s=100, label=f"Q{Q}")
plt.scatter(*M, color="purple", s=150, marker="*", label=f"M{M}")

# Annotate
plt.text(P[0]+0.2, P[1], f"P{P}", fontsize=10)
plt.text(Q[0]+0.2, Q[1], f"Q{Q}", fontsize=10)
plt.text(M[0]+0.2, M[1], f"M{M}", fontsize=10, color="purple")

# Axes
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.title("Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/4.3.14/figs/figure1.png")
plt.show()
