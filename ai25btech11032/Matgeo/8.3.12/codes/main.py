import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

# --- load shared lib ---
lib = ct.CDLL("./libellipse.so")
lib.ellipse_vuf.argtypes = [
    ct.POINTER(ct.c_double),  # F1
    ct.POINTER(ct.c_double),  # F2
    ct.c_double,              # sum (2a)
    ct.POINTER(ct.c_double),  # V (len 4, row-major)
    ct.POINTER(ct.c_double),  # u (len 2)
    ct.POINTER(ct.c_double),  # f (scalar)
]
lib.ellipse_vuf.restype = None

# --- problem data ---
F1 = np.array([3.0, 0.0], dtype=np.float64)
F2 = np.array([9.0, 0.0], dtype=np.float64)
sum_dist = 12.0  # 2a

# --- outputs ---
V = np.zeros(4, dtype=np.float64)  # row-major 2x2
u = np.zeros(2, dtype=np.float64)
f = np.zeros(1, dtype=np.float64)

# call C
lib.ellipse_vuf(
    F1.ctypes.data_as(ct.POINTER(ct.c_double)),
    F2.ctypes.data_as(ct.POINTER(ct.c_double)),
    ct.c_double(sum_dist),
    V.ctypes.data_as(ct.POINTER(ct.c_double)),
    u.ctypes.data_as(ct.POINTER(ct.c_double)),
    f.ctypes.data_as(ct.POINTER(ct.c_double)),
)

V2 = V.reshape(2,2)
print("V =\n", V2)
print("u =", u)
print("f =", f[0])

# --- derive c, f0, a, b from (V,u,f), exactly like theory ---
# c = -V^{-1} u
c = -np.linalg.solve(V2, u)

# f0 = u^T V^{-1} u - f
f0 = u @ np.linalg.solve(V2, u) - f[0]

# eigendecomposition V = P diag(lam) P^T
lam, P = np.linalg.eigh(V2)   # lam[0]<=lam[1]
# axes: a^2 = f0/lam1, b^2 = f0/lam2
a = np.sqrt(f0 / lam[0])
b = np.sqrt(f0 / lam[1])

print("center c =", c)
print("f0 =", f0)
print("semi-axes a, b =", a, b)

# --- plot from (V,u,f) ---
t = np.linspace(0, 2*np.pi, 600)
ellipse_local = np.vstack([a*np.cos(t), b*np.sin(t)])     # (2,N)
ellipse_global = (P @ ellipse_local).T + c                # rotate+shift

plt.plot(ellipse_global[:,0], ellipse_global[:,1], label="Ellipse")
plt.scatter([F1[0], F2[0]], [F1[1], F2[1]], label="Foci")
plt.scatter([c[0]], [c[1]], label="Center")

plt.gca().set_aspect("equal", adjustable="box")
plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1.0))
plt.grid(True)
plt.title("Matrix-form ellipse from C (.so) → Python")
plt.tight_layout()
plt.savefig("ellipse.png")
plt.show()

