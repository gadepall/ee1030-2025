import ctypes
from ctypes import c_double
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers 3D projection

# ---------- User inputs ----------
P = (2.0, 2.0, 1.0)   # Px,Py,Pz
Q = (5.0, 1.0, -2.0)  # Qx,Qy,Qz
Rx_given = 4.0        # given x-coordinate of R

# ---------- compute direction D = Q - P ----------
Px, Py, Pz = P
Qx, Qy, Qz = Q
Dx = Qx - Px
Dy = Qy - Py
Dz = Qz - Pz

if abs(Dx) < 1e-12:
    raise SystemExit("Error: Dx = 0. This script pivots on x; please pick a case with Dx != 0.")

# ---------- load C shared lib ----------
lib = ctypes.CDLL('./librow.so')
lib.compute_multiplier.argtypes = (c_double, c_double)
lib.compute_multiplier.restype = c_double
lib.apply_row_op.argtypes = (ctypes.POINTER(c_double),
                             ctypes.POINTER(c_double),
                             ctypes.POINTER(c_double))
lib.apply_row_op.restype = None

# ---------- call compute_multiplier in C ----------
a11 = float(Dx)              # r1[0]
a21 = float(Rx_given - Px)   # r2[0]
mult = lib.compute_multiplier(c_double(a11), c_double(a21))
print("Multiplier (from C) =", mult)

# ---------- compute y and z ----------
t = mult
y = Py + t * Dy
z = Pz + t * Dz
R = (Rx_given, y, z)
print("Computed R =", R)

# ---------- verify using apply_row_op ----------
r1 = (c_double * 3)(Dx, Dy, Dz)
r2 = (c_double * 3)(Rx_given - Px, y - Py, z - Pz)
out2 = (c_double * 3)()
lib.apply_row_op(r1, r2, out2)
out_list = [float(out2[i]) for i in range(3)]
print("Second row after elimination (from C apply_row_op):", out_list)

# ---------- plot P, Q, R with labels ----------
N = 101
ts = np.linspace(0.0, 1.0, N)
points = np.array([[Px + t*Dx, Py + t*Dy, Pz + t*Dz] for t in ts])

img3d = "line_3d.png"
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# line PQ
ax.plot(points[:,0], points[:,1], points[:,2], label='Line PQ')

# helper to format coordinates
def fmt_coords(pt):
    return f"({pt[0]:.2f}, {pt[1]:.2f}, {pt[2]:.2f})"

# points + labels
ax.scatter(*P, color='red', s=50)
ax.text(*P, f"P {fmt_coords(P)}", color='red', fontsize=10, weight='bold')

ax.scatter(*Q, color='blue', s=50)
ax.text(*Q, f"Q {fmt_coords(Q)}", color='blue', fontsize=10, weight='bold')

ax.scatter(*R, color='green', s=50)
ax.text(*R, f"R {fmt_coords(R)}", color='green', fontsize=10, weight='bold')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Line through P and Q with computed R')
plt.legend()

# save and show
plt.savefig(img3d, bbox_inches='tight')
print("Saved 3D image with P, Q, R labels ->", img3d)
plt.show()


