import ctypes
import math
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

# Load shared library
lib = ctypes.CDLL("./libnorm.so")

# Define function signatures
lib.find_intersection.argtypes = [ctypes.c_double, ctypes.c_double,
                                  ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.distance.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.distance.restype = ctypes.c_double

# Given point P
Px, Py = 4.0, 1.0

# Call C function to get Q
Qx = ctypes.c_double()
Qy = ctypes.c_double()
lib.find_intersection(Px, Py, ctypes.byref(Qx), ctypes.byref(Qy))
Qx, Qy = Qx.value, Qy.value

# Distance from C
dist = lib.distance(Px, Py, Qx, Qy)
print(f"distance: {dist:.3f} units")

# -----------------------------
# Plot same as before
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 6))

# Line y = 4x
x_line = [-1, 5]
y_line = [4*x for x in x_line]
ax.plot(x_line, y_line, label="Line: 4x - y = 0 (y=4x)")

# Direction line through P (slope -1)
x_dir = [Px - 4, Px + 4]
y_dir = [Py + 4, Py - 4]
ax.plot(x_dir, y_dir, linestyle="--", label="Direction 135° (slope -1)")

# Points P and Q
ax.plot(Px, Py, 'ro')
ax.annotate(f'P({Px:.0f},{Py:.0f})', xy=(Px,Py), xytext=(Px+0.2,Py-0.5))
ax.plot(Qx, Qy, 'mo')
ax.annotate(f'Q({Qx:.0f},{Qy:.0f})', xy=(Qx,Qy), xytext=(Qx+0.2,Qy+0.2))

# Segment PQ
ax.plot([Px, Qx], [Py, Qy], 'r-', linewidth=2)

# Distance label
mid = ((Px+Qx)/2, (Py+Qy)/2)
ax.text(mid[0], mid[1]+0.3, f'distance = {dist:.3f}', ha='center', color='red')

# Formatting
ax.set_aspect('equal', 'box')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True, alpha=0.4)
ax.legend(loc="upper right")


plt.savefig("/home/user/Matrix/Matgeo_assignments/4.7.12/figs/Figure_1.png")
plt.show()

