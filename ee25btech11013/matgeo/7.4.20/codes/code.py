import ctypes
import numpy as np 
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./libcode.so")

lib.xcenter.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.xcenter.restype = ctypes.c_int

lib.ycenter.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.ycenter.restype = ctypes.c_int

lib.dist.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.dist.restype = ctypes.c_double

c = np.array([-1, -1])

p = np.array([1, 0])


x = lib.xcenter(c[0], p[0], 2, -1)
y = lib.ycenter(c[1], p[1], 2, -1)
q = np.array([x, y])
print("The point Q is ", q)

r = lib.dist(c[0], c[1], p[0], p[1])

theta = np.linspace(0, 2*np.pi, 200)
circle_x = c[0] + r*np.cos(theta)
circle_y = c[1] + r*np.sin(theta)

fig, ax = plt.subplots()

ax.plot(circle_x, circle_y, color="blue", label="Circle")
ax.scatter([p[0], q[0]], [p[1], q[1]], color="red", label="Diameter Points")
ax.scatter(c[0], c[1], color="blue", marker="x", s=100, label="Center")

ax.plot([p[0], q[0]], [p[1], q[1]], "g--", label="Diameter")

ax.set_aspect("equal", adjustable="datalim")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.text(c[0], c[1], f"C({int(c[0])}, {int(c[1])})", fontsize=12, color="blue", ha="right", va="bottom")
ax.text(p[0], p[1], f"P({int(p[0])}, {int(p[1])})", fontsize=12, color="red", ha="left", va="top")
ax.text(q[0], q[1], f"Q({int(q[0])}, {int(q[1])})", fontsize=12, color="red", ha="right", va="top")



ax.legend()
ax.legend(loc="upper right")
ax.grid(True)
plt.savefig("/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/7.4.20/figs/Figure_1.png")
plt.show()
