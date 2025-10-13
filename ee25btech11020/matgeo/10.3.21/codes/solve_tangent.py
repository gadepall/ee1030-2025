import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./libsolve.so')

lib.tangent_point.argtypes = [ctypes.POINTER(ctypes.c_double)]

q = (ctypes.c_double * 2)()
lib.tangent_point(q)

qx, qy = q[0], q[1]
print(f"Point of Tangency: ({qx}, {qy})")

y = np.linspace(-4, 4, 400)
x = y**2 / 4

xt = np.linspace(0, 3, 100)
yt = xt + 1

plt.plot(x, y, 'b', linewidth=1.5)
plt.plot(xt, yt, 'r', linewidth=1.2)
plt.scatter(qx, qy, color='black', zorder=5)

plt.text(qx + 0.1, qy, f"P({qx:.0f},{qy:.0f})", fontsize=9)
plt.text(1.5, 2.7, "Tangent", color='r', fontsize=9)
plt.text(2, 3.5, "Parabola", color='b', fontsize=9)

plt.axhline(0, color='gray', linewidth=0.8)
plt.axvline(0, color='gray', linewidth=0.8)

plt.xlabel("x")
plt.ylabel("y")
plt.grid(False)
plt.axis("equal")

plt.savefig("../figs/img1.png", dpi=300, bbox_inches='tight')
plt.close()

