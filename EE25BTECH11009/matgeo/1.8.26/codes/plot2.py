import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
handc = ctypes.CDLL("./func.so")

# Define equidistant_yaxis prototype
handc.equidistant_yaxis.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
]
handc.equidistant_yaxis.restype = None

# Define line_gen prototype
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

# Points A and B
A = np.array([6.0, 5.0], dtype=np.float64)
B = np.array([-4.0, 3.0], dtype=np.float64)

# Placeholder for O
O = np.zeros(m, dtype=np.float64)

# Call C function to compute O
handc.equidistant_yaxis(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    O.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

print("A =", A)
print("B =", B)
print("O =", O)

# Generate lines
n = 20
X_l = np.zeros(n, dtype=np.float64)
Y_l = np.zeros(n, dtype=np.float64)

# AB
handc.line_gen(X_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               Y_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               n, m)
x_AB, y_AB = X_l.copy(), Y_l.copy()

# OA
handc.line_gen(X_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               Y_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               O.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               n, m)
x_OA, y_OA = X_l.copy(), Y_l.copy()

# OB
handc.line_gen(X_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               Y_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               O.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
               n, m)
x_OB, y_OB = X_l.copy(), Y_l.copy()

# Plotting
plt.figure()
plt.plot(x_AB, y_AB, "g--", label="Line AB")
plt.plot(x_OA, y_OA, "r--", label="Line OA")
plt.plot(x_OB, y_OB, "b--", label="Line OB")

# Points
plt.scatter(A[0], A[1], color="blue", s=50)
plt.scatter(B[0], B[1], color="red", s=50)
plt.scatter(O[0], O[1], color="green", s=50)

# Labels
plt.annotate(f"A({A[0]:.0f},{A[1]:.0f})", (A[0], A[1]), textcoords="offset points", xytext=(-20,10))
plt.annotate(f"B({B[0]:.0f},{B[1]:.0f})", (B[0], B[1]), textcoords="offset points", xytext=(10,-15))
plt.annotate(f"O({O[0]:.0f},{O[1]:.0f})", (O[0], O[1]), textcoords="offset points", xytext=(10,10))

# Equal aspect ratio
plt.gca().set_aspect("equal", adjustable="box")
plt.xlim([-8,8])
plt.ylim([0,12])

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Point O on y-axis equidistant from A and B")
plt.legend(loc="upper left")
plt.grid(True)

# Save & show
plt.savefig("../figs/equidistant_graph.png")
plt.show()
