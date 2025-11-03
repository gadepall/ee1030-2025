import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./vecs.so")

lib.line_vectors.argtypes = [ctypes.c_double,
                             ctypes.POINTER(ctypes.c_double),
                             ctypes.POINTER(ctypes.c_double)]

def get_vectors(m, c):
    mvec = (ctypes.c_double * 2)()
    nvec = (ctypes.c_double * 2)()
    lib.line_vectors(m, mvec, nvec)
    return np.array([mvec[0], mvec[1]]), np.array([nvec[0], nvec[1]])

m = 3
c = 0

mvec, nvec = get_vectors(m, c)
print("Direction vector m =", mvec)
print("Normal vector n =", nvec)

x_vals = np.linspace(-5, 5, 100)
y_vals = m * x_vals + c

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.plot(x_vals, y_vals, color="green")
plt.text(1+0.2, m*1 + c + 0.2, f"y={m}x+{c}", color="green")

plt.quiver(0, 0, mvec[0], mvec[1], angles='xy', scale_units='xy', scale=1, color='red')
plt.text(mvec[0]*0.6, mvec[1]*0.6, "Direction", color="red")

plt.quiver(0, 0, nvec[0], nvec[1], angles='xy', scale_units='xy', scale=1, color='blue')
plt.text(nvec[0]*0.6, nvec[1]*0.6, "Normal", color="blue")

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
