import ctypes
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load shared library
lib = ctypes.CDLL('./liblines.so')
lib.perpendicular_lambda.restype = ctypes.c_double
lib.intersection_lambda.restype = ctypes.c_double
lib.lines_intersection_params.restype = ctypes.c_int
lib.lines_intersection_params.argtypes = [
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

# 1. Get lambdas
lam_perp = lib.perpendicular_lambda()
lam_inter = lib.intersection_lambda()

print(f"Lambda for perpendicular lines: {lam_perp} = {Fraction(lam_perp).limit_denominator()}")
print(f"Lambda for intersection: {lam_inter} = {Fraction(lam_inter).limit_denominator()}")

# 2. Check intersection at perpendicular lambda
s1 = ctypes.c_double()
t1 = ctypes.c_double()
intersects_perp = lib.lines_intersection_params(lam_perp, ctypes.byref(s1), ctypes.byref(t1))

# 3. Check intersection at intersection lambda
s2 = ctypes.c_double()
t2 = ctypes.c_double()
intersects = lib.lines_intersection_params(lam_inter, ctypes.byref(s2), ctypes.byref(t2))

if intersects_perp:
    print("Lines intersect when perpendicular.")
else:
    print("❌ Lines do NOT intersect when they are perpendicular.")

if intersects:
    print("✅ Lines intersect when λ =", lam_inter)
    print("Intersection parameters: s =", s2.value, ", t =", t2.value)
    inter_point = np.array([
        s2.value,
        -0.5 + 2*lam_inter*s2.value,
        1 + 3*s2.value
    ])
    print("Intersection point:", inter_point)
else:
    inter_point = None
    print("❌ Lines do NOT intersect for intersection λ.")

# 4. Plot
t_vals = np.linspace(-2, 2, 100)
x1 = 5 + (5*lam_inter + 2)*t_vals
y1 = 2 - 5*t_vals
z1 = 1 + t_vals

s_vals = np.linspace(-2, 2, 100)
x2 = s_vals
y2 = -0.5 + 2*lam_inter*s_vals
z2 = 1 + 3*s_vals

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot lines
ax.plot(x1, y1, z1, label="Line 1", color='blue', linewidth=2)
ax.plot(x2, y2, z2, label="Line 2", color='red', linewidth=2)

# Plot intersection
if inter_point is not None:
    ax.scatter(*inter_point, color='green', s=80, edgecolors='black', label="Intersection Point")
    ax.text(*inter_point + 0.3, 
            f"({inter_point[0]:.2f}, {inter_point[1]:.2f}, {inter_point[2]:.2f})",
            fontsize=10, color='green')

# Labels and legend
ax.set_xlabel("X Axis", fontsize=12)
ax.set_ylabel("Y Axis", fontsize=12)
ax.set_zlabel("Z Axis", fontsize=12)
ax.set_title("3D Plot: Intersection of Two Lines", fontsize=14)
ax.legend()
ax.grid(True)
ax.view_init(elev=25, azim=135)

plt.tight_layout()
plt.show()

