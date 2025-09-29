#!/usr/bin/env python3
import os
import subprocess
import ctypes
import math
import matplotlib.pyplot as plt

C_FILE = "section.c"
SO_FILE = "./libsection.so"

# Auto-compile if shared lib not present
if not os.path.exists(SO_FILE):
    print("libsection.so not found — compiling section.c ...")
    cmd = ["gcc", "-shared", "-o", "libsection.so", "-fPIC", C_FILE]
    try:
        subprocess.run(cmd, check=True)
        print("Compiled libsection.so")
    except subprocess.CalledProcessError as e:
        print("Compilation failed:", e)
        raise SystemExit(1)

# Load shared library
lib = ctypes.CDLL(SO_FILE)

# Set function signature:
# void section_point(double, double, double, double, double,
#                    double*, double*, double*)
lib.section_point.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double,
                              ctypes.c_double,
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]
lib.section_point.restype = None

# Input points
Ax, Ay = -5.0, 8.0
Bx, By =  4.0, -10.0
yP = 4.0

# Prepare output holders
ratio_AP = ctypes.c_double()
ratio_PB = ctypes.c_double()
xP = ctypes.c_double()

# Call C function
lib.section_point(Ax, Ay, Bx, By, yP,
                  ctypes.byref(ratio_AP),
                  ctypes.byref(ratio_PB),
                  ctypes.byref(xP))

# Read outputs
m = ratio_AP.value  # AP vertical distance (Ay - yP)
n = ratio_PB.value  # PB vertical distance (yP - By)
x_val = xP.value

# Convert ratio to smallest integer ratio (if sensible)
# We'll round to nearest integer then reduce by gcd if both nonzero
def reduced_ratio(a, b):
    ia = int(round(a))
    ib = int(round(b))
    if ia == 0 and ib == 0:
        return (0, 0)
    if ia < 0: ia = -ia
    if ib < 0: ib = -ib
    g = math.gcd(ia, ib) if (ia != 0 and ib != 0) else (ia or ib)
    if g == 0:
        return (ia, ib)
    return (ia // g, ib // g)

ratA_int, ratB_int = reduced_ratio(m, n)

print(f" Raw m (AP) = {m}, n (PB) = {n}")
print(f" AP:PB (reduced) = {ratA_int}:{ratB_int}")
print(f" x = {x_val}")

# ---- Plot ----
A = (Ax, Ay)
B = (Bx, By)
P = (x_val, yP)

plt.plot([A[0], B[0]], [A[1], B[1]], linestyle='--', label="Line AB")
plt.scatter(*A, marker='o', label=f"A{A}", zorder=5)
plt.scatter(*B, marker='o', label=f"B{B}", zorder=5)
plt.scatter(*P, marker='o', label=f"P({x_val:.3g},{yP})", zorder=5)

plt.text(A[0]-0.6, A[1]+0.4, f"A{A}", color="red")
plt.text(B[0]+0.4, B[1]-0.6, f"B{B}", color="blue")
plt.text(P[0]+0.4, P[1]+0.4, f"P({x_val:.3g},{yP})", color="green")

plt.axhline(0, color="gray", lw=0.5)
plt.axvline(0, color="gray", lw=0.5)
plt.grid(True, linestyle="--", alpha=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"P divides AB in ratio {ratA_int}:{ratB_int}")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

