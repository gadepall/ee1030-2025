import ctypes
from ctypes import c_double, c_int, POINTER
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./mg4.so")   # works if mg4.so is in the same folder
# 2) Declare C signatures
lib.arr_dot.argtypes  = [POINTER(c_double), POINTER(c_double), c_int]
lib.arr_dot.restype   = c_double
lib.arr_norm.argtypes = [POINTER(c_double), c_int]
lib.arr_norm.restype  = c_double
lib.arr_normalize.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
lib.arr_normalize.restype  = None
lib.line_direction_normal.argtypes = [c_double, c_double, c_double,
                                      POINTER(c_double), POINTER(c_double)]
lib.line_direction_normal.restype  = None

# Small helpers to pass arrays to C
def cvec(arr):
    arr = np.asarray(arr, dtype=float)
    return (c_double * arr.size)(*arr.tolist()), arr.size

def dot(u, v):
    cu, n = cvec(u); cv, _ = cvec(v)
    return lib.arr_dot(cu, cv, n)

def normalize(u):
    cu, n = cvec(u)
    out = (c_double * n)()
    lib.arr_normalize(cu, out, n)
    return np.array([out[i] for i in range(n)], dtype=float)

# 3) Solve x - y = 2  (a=1, b=-1, c=2)
a, b, c = 1.0, -1.0, 2.0
d = (c_double * 2)()
n = (c_double * 2)()
lib.line_direction_normal(a, b, c, d, n)

d_np = np.array([d[0], d[1]])
n_np = np.array([n[0], n[1]])
ud = normalize(d_np)
un = normalize(n_np)

print("Direction (raw):", d_np.tolist())   # [1.0, 1.0]
print("Normal   (raw):", n_np.tolist())    # [1.0, -1.0]
print("dot(direction, normal) =", dot(d_np, n_np))  # 0.0

# 4) Plot
x = np.linspace(-2, 6, 200)
y = x - 2
x0, y0 = 2.0, 0.0
scale = 2.0

plt.figure()
plt.plot(x, y, label="x - y = 2")
plt.quiver([x0], [y0], [ud[0]*scale], [ud[1]*scale],
           angles='xy', scale_units='xy', scale=1, label="direction")
plt.quiver([x0], [y0], [un[0]*scale], [un[1]*scale],
           angles='xy', scale_units='xy', scale=1, label="normal")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("x"); plt.ylabel("y")
plt.title("Line x - y = 2 with direction and normal vectors")
plt.grid(True); plt.legend()
plt.show()
