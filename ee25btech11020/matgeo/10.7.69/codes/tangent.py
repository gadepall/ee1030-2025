import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

libname = "./libtangent.so"
if not os.path.exists(libname):
    raise FileNotFoundError("Compile tangent.c first to create libtangent.so")

lib = ctypes.CDLL(libname)
compute = lib.compute_tangents
compute.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                    ctypes.c_double, ctypes.c_double,
                    ctypes.POINTER(ctypes.c_double)]
compute.restype = None

out_arr = (ctypes.c_double * 9)()
compute(2.0, 1.0, 4.0, 4.0, 5.0, out_arr)

area = out_arr[0]
xt1, yt1 = out_arr[1], out_arr[2]
m1, c1 = out_arr[3], out_arr[4]
xt2, yt2 = out_arr[5], out_arr[6]
m2, c2 = out_arr[7], out_arr[8]

print("Area =", area)
print("T1 =", (xt1, yt1), "line params:", (m1, c1))
print("T2 =", (xt2, yt2), "line params:", (m2, c2))

h, k, r = 2.0, 1.0, 4.0
theta = np.linspace(0, 2*np.pi, 400)
xc = h + r*np.cos(theta)
yc = k + r*np.sin(theta)
# --- Plot the circle, tangents, and points ---
plt.figure(figsize=(7, 7))

# Circle
plt.plot(xc, yc, 'b-', label='Circle (center=(2,1), r=4)')

# Center and external point
plt.scatter([2], [1], color='k', s=40, label='Center O(2,1)')
plt.scatter([4], [5], color='r', s=50, label='External Point P(4,5)')

# Tangent points
plt.scatter([xt1, xt2], [yt1, yt2], color='g', s=60, label='Tangent Points (T₁, T₂)')

# Tangent lines (handle vertical)
xs = np.linspace(-3, 9, 400)
def plot_line(m, c, label):
    if np.isinf(m) or abs(m) > 1e8:
        plt.axvline(c, linestyle='--', label=label)
    else:
        plt.plot(xs, m*xs + c, '--', label=label)

plot_line(m1, c1, f"Tangent 1: y = {m1:.2f}x + {c1:.2f}")
plot_line(m2, c2, f"Tangent 2: y = {m2:.2f}x + {c2:.2f}")

# Fix view limits so entire circle + tangents visible
plt.xlim(-3, 10)
plt.ylim(-4, 9)

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend(loc='upper right')
plt.title(f"Tangents from P(4,5) to circle\nArea of quadrilateral = {area:.2f}")
plt.savefig("../figs/img1.png")
