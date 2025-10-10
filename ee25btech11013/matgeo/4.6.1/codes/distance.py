import numpy as np
import matplotlib.pyplot as plt
import ctypes


lib = ctypes.CDLL("./libdistance.so")


lib.plane_distance.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.c_double]
lib.plane_distance.restype = ctypes.c_double


n = np.array([2.0, 1.0, -2.0], dtype=np.double)
a = -6.0
b = 0.0


n_ptr = n.ctypes.data_as(ctypes.POINTER(ctypes.c_double))


dist = lib.plane_distance(n_ptr, a, b)
print("Distance =", dist)


fig = plt.figure()
ax3d = fig.add_subplot(projection="3d")

x, y = np.meshgrid(range(-10, 11), range(-10, 11))

z1 = (2*x + y - 6) / 2
z2 = (2*x + y) / 2

ax3d.plot_surface(x, y, z1, alpha=0.5, color='blue')
ax3d.plot_surface(x, y, z2, alpha=0.5, color='red')

ax3d.plot([], [], [], color='blue', label="2x + y - 2z - 6 = 0")
ax3d.plot([], [], [], color='red', label="2x + y - 2z = 0")

ax3d.set_xlabel("X")
ax3d.set_ylabel("Y")
ax3d.set_zlabel("Z")
ax3d.set_title(f"Two Parallel Planes\nDistance = {dist}")
ax3d.legend(loc='upper right')

plt.savefig("/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/4.6.1/figs/Figure_1.png")
plt.show()
