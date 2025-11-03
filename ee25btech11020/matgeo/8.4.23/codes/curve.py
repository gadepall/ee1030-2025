import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./libcurve.so')

lib.check_parabola.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64),
    np.ctypeslib.ndpointer(dtype=np.float64),
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double
]

n = 200
x = np.zeros(n, dtype=np.float64)
y = np.zeros(n, dtype=np.float64)

lib.check_parabola(x, y, n, -10.0, 10.0)
plt.figure(figsize=(6,6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Parabola: x = t² + t + 1, y = t² - t + 1')
plt.grid(True)

plt.savefig('../figs/img1.png', dpi=300, bbox_inches='tight')
plt.close()

