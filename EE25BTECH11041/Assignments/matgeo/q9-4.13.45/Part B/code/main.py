# main.py
# Usage:
# 1. Compile C: gcc -shared -o libbisector.so -fPIC main.c -lm
# 2. Run: python3 main.py

import ctypes
from ctypes import Structure, c_double
import numpy as np
import matplotlib.pyplot as plt
import math
import os

# define Line struct to match C
class Line(Structure):
    _fields_ = [("a", c_double), ("b", c_double), ("c", c_double)]

# load shared library (adjust path if necessary)
libpath = "./libbisector.so"
if not os.path.exists(libpath):
    raise RuntimeError(f"Shared object {libpath} not found. Compile main.c first.")

lib = ctypes.CDLL(libpath)
lib.obtuse_bisector.restype = Line
lib.obtuse_bisector.argtypes = [c_double,c_double,c_double,c_double,c_double,c_double]

# Given lines
# L1: x - 2y + 4 = 0  => a1=1, b1=-2, c1=4
# L2: 4x - 3y + 2 = 0 => a2=4, b2=-3, c2=2
a1, b1, c1 = 1.0, -2.0, 4.0
a2, b2, c2 = 4.0, -3.0, 2.0

# call C function
res = lib.obtuse_bisector(a1,b1,c1,a2,b2,c2)
A, B, C = res.a, res.b, res.c

# print equation in nicer form (scale back to readable)
# We'll scale so that coefficients are not tiny; find max abs
scale = max(abs(A), abs(B), abs(C))
if scale < 1e-12: scale = 1.0
A_s, B_s, C_s = A/scale, B/scale, C/scale

print("Computed (normalized) obtuse-angle bisector coefficients:")
print(f"A = {A:.6f}, B = {B:.6f}, C = {C:.6f}")
print(f"Equation: ({A_s:.6f}) x + ({B_s:.6f}) y + ({C_s:.6f}) = 0   (scaled)")

# Compute intersection point of L1 and L2 for plotting center
D = a1*b2 - a2*b1
if abs(D) < 1e-12:
    print("Given lines are parallel or nearly parallel; cannot find intersection.")
    Px = Py = 0.0
else:
    Px = (b1*c2 - b2*c1) / D
    Py = (a2*c1 - a1*c2) / D
    print(f"Intersection point: P = ({Px:.6f}, {Py:.6f})")

# Prepare plotting
# produce a range around intersection
rng = 10
xs = np.linspace(Px - rng, Px + rng, 400)

# function to produce y from ax+by+c=0 -> y = (-a x - c)/b if b!=0 else None
def line_y(a,b,c, xvals):
    if abs(b) < 1e-12:
        return None
    return [(-a*x - c)/b for x in xvals]

y1 = line_y(a1,b1,c1, xs)
y2 = line_y(a2,b2,c2, xs)
yB = line_y(A,B,C, xs)

plt.figure(figsize=(8,8))
if y1 is not None:
    plt.plot(xs, y1, label="L1: x - 2y + 4 = 0", linewidth=2)
else:
    # vertical line x = -c/a
    xv = -c1/a1
    plt.axvline(x=xv, label="L1 (vertical)")

if y2 is not None:
    plt.plot(xs, y2, label="L2: 4x - 3y + 2 = 0", linewidth=2)
else:
    xv = -c2/a2
    plt.axvline(x=xv, label="L2 (vertical)")

if yB is not None:
    plt.plot(xs, yB, '--', label="Obtuse-angle bisector", linewidth=2)
else:
    xv = -C/A
    plt.axvline(x=xv, linestyle='--', label="Obtuse bisector (vertical)")

# plot intersection point
plt.scatter([Px],[Py], color='k')
plt.text(Px, Py, '  P(intersection)', fontsize=9)

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lines and the Obtuse-angle Bisector')
plt.axis('equal')
plt.show()

