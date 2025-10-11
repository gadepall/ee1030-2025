import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./libplanes.so")

lib.find_planes.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.POINTER((ctypes.c_double * 4) * 2)
]

n1 = np.array([1, 3, 0], dtype=float)    # x + 3y - 6 = 0
n2 = np.array([3, -1, -4], dtype=float)  # 3x - y - 4z = 0
c = ctypes.c_double(6)

n1_c = (ctypes.c_double * 3)(*n1)
n2_c = (ctypes.c_double * 3)(*n2)
result = ((ctypes.c_double * 4) * 2)()
lib.find_planes(n1_c, n2_c, c, result)
planes = np.array(result, dtype=float)

print("Required planes (a,b,c,d):")
for i, coeffs in enumerate(planes):
    a, b, c_, d = coeffs
    print(f"Plane {i+1}: {a:.2f}x + {b:.2f}y + {c_:.2f}z {d:+.2f} = 0")

d_vec = np.cross(n1, n2)
d_vec = d_vec / np.linalg.norm(d_vec)

y0 = 0
x0 = 6 - 3*y0
z0 = (3*x0 - y0) / 4
point_on_line = np.array([x0, y0, z0], dtype=float)
t_vals = np.linspace(-5, 5, 50)
line_points = point_on_line[:, None] + d_vec[:, None] * t_vals

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection='3d')
xx, yy = np.meshgrid(np.linspace(-5,5,40), np.linspace(-5,5,40))
ax.view_init(elev=25,azim=65)
zz1 = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz1, alpha=0.3, color="green")
ax.text(2, 2, 0, "Given 1", color="green", fontsize=11)

zz2 = (-3*xx + yy)/4
ax.plot_surface(xx, yy, zz2, alpha=0.3, color="blue")
ax.text(2, -2, (-3*2 + -2)/4, "Given 2", color="blue", fontsize=11)

ax.plot(line_points[0], line_points[1], line_points[2], color="purple", linewidth=2)
ax.text(*point_on_line, "Intersection", color="purple", fontsize=11)

for i, coeffs in enumerate(planes):
    a, b, c_, d = coeffs
    if abs(c_) < 1e-6:
        continue
    zz = (-a*xx - b*yy - d)/c_
    ax.plot_surface(xx, yy, zz, alpha=0.4, color="red")
    ax.text(2, 2, (-a*2 - b*2 - d)/c_, f"Req {i+1}", color="red", fontsize=11)

ax.scatter(0,0,0, color="black", s=60)
ax.text(0.2,0.2,0.2,"Origin", color="black", fontsize=11)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.tight_layout()
plt.savefig("../figs/img1.png", dpi=300)
