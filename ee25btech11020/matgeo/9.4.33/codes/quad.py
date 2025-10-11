import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./libquad.so')

lib.solve_quadratic.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

a, b, c = 1.0, -4.0, 3.0

r1 = ctypes.c_double()
r2 = ctypes.c_double()

lib.solve_quadratic(a, b, c, ctypes.byref(r1), ctypes.byref(r2))

x1, x2 = r1.value, r2.value
print(f"Roots: x1 = {x1}, x2 = {x2}")

x = np.linspace(0, 4, 400)
y = a*x**2 + b*x + c

plt.figure(figsize=(6,4))
plt.plot(x, y, 'b', linewidth=2)
plt.axhline(0, color='black', linewidth=1)

plt.scatter([x1, x2], [0, 0], color='red')
plt.text(x1, 0.2, f'({x1:.1f},0)', ha='center', fontsize=9)
plt.text(x2, 0.2, f'({x2:.1f},0)', ha='center', fontsize=9)

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.savefig("../figs/img1.png", dpi=300, bbox_inches='tight')
plt.close()

