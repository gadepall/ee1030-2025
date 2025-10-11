import numpy as np
import matplotlib.pyplot as plt
import ctypes

lines_lib = ctypes.CDLL('./points.so')

n = 100
x = np.linspace(-5, 15, n)
y1 = np.zeros(n, dtype=np.float64)
y2 = np.zeros(n, dtype=np.float64)


lines_lib.get_lines.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    ctypes.c_int
]
lines_lib.get_lines(x, y1, y2, n)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='red')
plt.text(10, 20, r'$3x - y = 3$', color='blue', fontsize=12)
plt.text(7.5, 35, r'$4x - y = 8$', color='red', fontsize=12)

plt.title("System of Equations")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
