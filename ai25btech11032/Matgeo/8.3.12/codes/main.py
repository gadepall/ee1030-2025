import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
# On macOS, use: lib = ct.CDLL("./libellipse_simple.dylib")
lib = ct.CDLL("./libellipse_simple.so")

# Set function signature
lib.ellipse_params.argtypes = [
    ct.POINTER(ct.c_double),  # F1
    ct.POINTER(ct.c_double),  # F2
    ct.c_double,              # sum (2a)
    ct.POINTER(ct.c_double),  # V (len 4, row-major)
    ct.POINTER(ct.c_double),  # u (len 2)
    ct.POINTER(ct.c_double),  # f (scalar)
    ct.POINTER(ct.c_double),  # c (len 2)
    ct.POINTER(ct.c_double),  # a_out (scalar)
    ct.POINTER(ct.c_double),  # b_out (scalar)
]
lib.ellipse_params.restype = None

# Inputs (your problem)
F1 = np.array([3.0, 0.0], dtype=np.float64)
F2 = np.array([9.0, 0.0], dtype=np.float64)
sum_dist = 12.0

# Outputs
V = np.zeros(4, dtype=np.float64)
u = np.zeros(2, dtype=np.float64)
f = np.zeros(1, dtype=np.float64)
c = np.zeros(2, dtype=np.float64)
a = np.zeros(1, dtype=np.float64)
b = np.zeros(1, dtype=np.float64)

# Call the C function
lib.ellipse_params(
    F1.ctypes.data_as(ct.POINTER(ct.c_double)),
    F2.ctypes.data_as(ct.POINTER(ct.c_double)),
    ct.c_double(sum_dist),
    V.ctypes.data_as(ct.POINTER(ct.c_double)),
    u.ctypes.data_as(ct.POINTER(ct.c_double)),
    f.ctypes.data_as(ct.POINTER(ct.c_double)),
    c.ctypes.data_as(ct.POINTER(ct.c_double)),
    a.ctypes.data_as(ct.POINTER(ct.c_double)),
    b.ctypes.data_as(ct.POINTER(ct.c_double)),
)

# Show computed parameters
print("V =\n", V.reshape(2,2))
print("u =", u)
print("f =", f[0])
print("center c =", c)
print("a, b =", a[0], b[0])

# Parametric plot (simple & direct)
t = np.linspace(0, 2*np.pi, 600)
x = c[0] + a[0]*np.cos(t)
y = c[1] + b[0]*np.sin(t)

plt.plot(x, y, label="Locus")
plt.scatter([F1[0], F2[0]], [F1[1], F2[1]], label="Foci")
plt.scatter([c[0]], [c[1]], label="Center")
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True)
plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1.0))
plt.title("Locus from .so (first principles) → Plot")
plt.tight_layout()
plt.savefig("ellipse.png")
plt.show()

