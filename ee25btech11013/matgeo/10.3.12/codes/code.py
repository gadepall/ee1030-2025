import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./libcode.so')

lib.compute_x.argtypes = []
lib.compute_x.restype = ctypes.c_double

lib.compute_y.argtypes = [ctypes.c_double]
lib.compute_y.restype = ctypes.c_double

lib.compute_k.argtypes = [ctypes.c_double, ctypes.c_double]
lib.compute_k.restype = ctypes.c_double

x = lib.compute_x()
y = lib.compute_y(x)
K = lib.compute_k(x, y)
q = np.array([x, y])
x_vals = np.linspace(-50, 50, 400)
y_parabola = x_vals**2 / 16
y_line = np.sqrt(3) * x_vals + K

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_parabola, label=r'$x^2 = 16y$', color='blue')
plt.plot(x_vals, y_line, label=rf'$y = \sqrt{{3}}x {K:.0f}$', color='red', linestyle='--')
plt.plot(q[0], q[1], 'ko', label='Point of Contact')
plt.text(q[0], q[1], f'({q[0]:.2f}, {q[1]:.2f})', fontsize=9, ha='center', va='center')
plt.title("Parabola and Tangent Line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/10.3.12/figs/Figure_1.png")
plt.show()

