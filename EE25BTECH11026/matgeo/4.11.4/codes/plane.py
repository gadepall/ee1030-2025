import ctypes
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import matplotlib as mp
from fractions import Fraction
import math

mp.use("TkAgg")

# ------------------------
# Load shared library
# ------------------------
lib = ctypes.CDLL("./libplane.so")

# Define argtypes and restype
lib.required_plane.argtypes = [
    ctypes.POINTER(ctypes.c_double), ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
lib.required_plane.restype = None

# ------------------------
# Input planes
# ------------------------
n1 = (ctypes.c_double * 3)(1, 2, 3)
d1 = -4.0
n2 = (ctypes.c_double * 3)(2, 1, -1)
d2 = 5.0
n3 = (ctypes.c_double * 3)(5, 3, -6)
d3 = 8.0

# ------------------------
# Output storage
# ------------------------
n_req = (ctypes.c_double * 3)()
d_req = ctypes.c_double()

# Call C function
lib.required_plane(n1, d1, n2, d2, n3, d3, n_req, ctypes.byref(d_req))

# Convert to numpy + sympy
n_req_np = np.array([n_req[i] for i in range(3)], dtype=float)
d_req_val = float(d_req.value)
n_vec = sp.Matrix(n_req_np)

# ------------------------
# Formatting helpers
# ------------------------
def format_plane_integer(n, d):
    # Fractions for exactness
    n_frac = [Fraction(str(float(v))).limit_denominator() for v in n]
    d_frac = Fraction(str(float(d))).limit_denominator()

    # LCM of denominators
    denoms = [f.denominator for f in n_frac] + [d_frac.denominator]
    lcm = math.lcm(*denoms)

    n_int = [int(f * lcm) for f in n_frac]
    d_int = int(d_frac * lcm)

    # ---- Fix sign convention ----
    # Equation is n·r + d = 0  →  n·r = -d
    rhs = -d_int

    # Make gcd simplification
    g = math.gcd(math.gcd(abs(n_int[0]), abs(n_int[1])), math.gcd(abs(n_int[2]), abs(rhs)))
    n_int = [ni // g for ni in n_int]
    rhs //= g

    return f"r · ({n_int[0]}, {n_int[1]}, {n_int[2]}) = {rhs}"

# ------------------------
# Step 5: Vector form
# ------------------------
x, y, z = sp.symbols('x y z')
plane_eq = n_vec[0]*x + n_vec[1]*y + n_vec[2]*z + d_req_val

# ------------------------
# Output
# ------------------------
print("\nEquation of required plane:")
print(format_plane_integer(n_req_np, d_req_val))

# ------------------------
# Step 6: Plot planes
# ------------------------
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

def plot_plane(ax, n, d, color, alpha=0.4):
    xx, yy = np.meshgrid(np.linspace(-5,5,15), np.linspace(-5,5,15))
    zz = (-n[0]*xx - n[1]*yy - d) / n[2]
    ax.plot_surface(xx, yy, zz, color=color, alpha=alpha)

# Convert sympy / ctypes → float numpy
n1f, d1f = np.array([1,2,3], dtype=float), -4.0
n2f, d2f = np.array([2,1,-1], dtype=float), 5.0
n3f, d3f = np.array([5,3,-6], dtype=float), 8.0
nrf = n_req_np
drf = d_req_val

# Plot given planes and required plane
plot_plane(ax, n1f, d1f, "red", 0.2)     # π1
plot_plane(ax, n2f, d2f, "blue", 0.2)    # π2
plot_plane(ax, n3f, d3f, "green", 0.2)   # π3
plot_plane(ax, nrf, drf, "purple", 0.6)  # Required plane

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(r"Required Plane through Intersection, $\perp$ to Given Plane")

plt.savefig("/home/user/Matrix/Matgeo_assignments/4.11.4/figs/Figure_1", dpi=300, bbox_inches="tight")
plt.show()

