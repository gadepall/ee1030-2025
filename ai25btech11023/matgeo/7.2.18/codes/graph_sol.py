import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

lib = ctypes.CDLL(os.path.abspath("./libgraph.so"))
lib.set_params.argtypes = [ctypes.c_double, ctypes.c_double]
lib.compute_circle.argtypes = [ctypes.c_double,
                               ctypes.POINTER(ctypes.c_double),
                               ctypes.POINTER(ctypes.c_double)]

a, b = 4.0, 3.0
lib.set_params(a, b)

theta_vals = np.linspace(0, 2 * np.pi, 400)
x_vals, y_vals = [], []

for theta in theta_vals:
    x = ctypes.c_double()
    y = ctypes.c_double()
    lib.compute_circle(theta, ctypes.byref(x), ctypes.byref(y))
    x_vals.append(x.value)
    y_vals.append(y.value)

plt.plot(x_vals, y_vals, label="Full Circle")
plt.title(f"Circle through origin with x-intercept {a} and y-intercept {b}")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()
plt.savefig('../figs/fig.png')
