import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

# --- load the shared library (same folder) ---
lib = ct.CDLL("./libsimple_conic.so")

# tell ctypes what arguments the C function expects
lib.intersect_line_conic.argtypes = [
    ct.POINTER(ct.c_double),  # V[4]
    ct.POINTER(ct.c_double),  # u[2]
    ct.c_double,              # f
    ct.POINTER(ct.c_double),  # h[2]
    ct.POINTER(ct.c_double),  # m[2]
    ct.POINTER(ct.c_double),  # kappa[2] out
    ct.POINTER(ct.c_double),  # x1[2] out
    ct.POINTER(ct.c_double),  # x2[2] out
    ct.POINTER(ct.c_int)      # status out
]
lib.intersect_line_conic.restype = None

# ---- helper: convert quadratic ax^2+bx+c into conic form ----
def quadratic_to_conic(a, b, c):
    V = np.array([a, 0.0, 0.0, 0.0], dtype=np.double)     # [[a,0],[0,0]]
    u = np.array([b/2.0, 0.0], dtype=np.double)           # so 2u^T x = b x
    f = np.double(c)
    return V, u, f

# ---- our quadratic: x^2 - 3x - 10 = 0 ----
a, b, c = 1.0, -3.0, -10.0
V, u, f = quadratic_to_conic(a, b, c)

# Intersect with x-axis (y=0): line x = h + k m
h = np.array([0.0, 0.0], dtype=np.double)
m = np.array([1.0, 0.0], dtype=np.double)

# Outputs (allocated for C)
kappa = np.zeros(2, dtype=np.double)
x1 = np.zeros(2, dtype=np.double)
x2 = np.zeros(2, dtype=np.double)
status = ct.c_int(0)

# ---- call the C function ----
lib.intersect_line_conic(
    V.ctypes.data_as(ct.POINTER(ct.c_double)),
    u.ctypes.data_as(ct.POINTER(ct.c_double)),
    ct.c_double(f),
    h.ctypes.data_as(ct.POINTER(ct.c_double)),
    m.ctypes.data_as(ct.POINTER(ct.c_double)),
    kappa.ctypes.data_as(ct.POINTER(ct.c_double)),
    x1.ctypes.data_as(ct.POINTER(ct.c_double)),
    x2.ctypes.data_as(ct.POINTER(ct.c_double)),
    ct.byref(status)
)

# Collect results
roots = []
if status.value >= 1:
    roots.append(float(x1[0]))
    if status.value == 2:
        roots.append(float(x2[0]))
roots.sort()
print("status:", status.value)
print("roots:", roots)  # expected [-2.0, 5.0]

# ---- plot parabola and roots ----
xs = np.linspace(-10, 10, 600)     # simpler fixed range
ys = a*xs*xs + b*xs + c

plt.figure()
plt.plot(xs, ys, label=rf"$y={a:.0f}x^2{b:+.0f}x{c:+.0f}$")
plt.axhline(0, linestyle="--", linewidth=1, label="x-axis")
for r in roots:
    plt.scatter([r], [0.0], s=60, zorder=3, label=f"root {r:g}")
plt.xlabel("x"); plt.ylabel("y")
plt.title("Roots via line–conic intersection (NumPy + C)")
plt.grid(True)
plt.legend()
plt.savefig("parabola.png")
plt.show()

