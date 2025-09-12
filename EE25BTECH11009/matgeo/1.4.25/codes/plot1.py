import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
handc = ctypes.CDLL("./func.so")

# section function
handc.section.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
]
handc.section.restype = None

# line_gen function
handc.line_gen.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
    ctypes.c_int
]
handc.line_gen.restype = None

# Dimension
m = 2

# Define basis vectors
a = np.array([1,0], dtype=np.float64)
b = np.array([0,1], dtype=np.float64)

# Define P = 2a + b, Q = a - 3b
P = 2*a + b
Q = a - 3*b

# Placeholder for R
R = np.zeros(m, dtype=np.float64)

# Call C function for section
handc.section(
    P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    Q.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    R.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    m
)

print("P =", P)
print("Q =", Q)
print("R =", R)

# Generate line PQ
n = 20
X_l = np.zeros(n, dtype=np.float64)
Y_l = np.zeros(n, dtype=np.float64)

handc.line_gen(
    X_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    Y_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    Q.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    R.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    n, m
)

# Plotting
plt.figure()

# Line PQ
plt.plot(X_l, Y_l, "g--", label="Line PQ")

# Points
plt.scatter(P[0], P[1], color="blue", s=50)
plt.scatter(Q[0], Q[1], color="green", s=50)
plt.scatter(R[0], R[1], color="red", s=50, label="R (external division)")

# Labels
plt.annotate(f"P({P[0]},{P[1]})", (P[0], P[1]), textcoords="offset points", xytext=(-20,10))
plt.annotate(f"Q({Q[0]},{Q[1]})", (Q[0], Q[1]), textcoords="offset points", xytext=(10,-15))
plt.annotate(f"R({R[0]},{R[1]})", (R[0], R[1]), textcoords="offset points", xytext=(10,10))

# Equal aspect ratio
plt.gca().set_aspect("equal", adjustable="box")
plt.xlim([-4,7])
plt.ylim([-5,6])

plt.xlabel("X")
plt.ylabel("Y")
plt.title("External Division of Line PQ (Ratio 1:2)")
plt.legend(loc="upper left")
plt.grid(True)

# Save & show
plt.savefig("../figs/section_graph.png")
plt.show()
