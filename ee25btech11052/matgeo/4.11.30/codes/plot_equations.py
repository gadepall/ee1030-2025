import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./libequations.so")

lib.solve_equations.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

x = ctypes.c_double()
y = ctypes.c_double()

lib.solve_equations(ctypes.byref(x), ctypes.byref(y))

print(f"Solution from C: x = {x.value}, y = {y.value}")

xx = np.linspace(-2, 6, 100)

y1 = xx + 1

y2 = (12 - 3*xx) / 2

plt.plot(xx, y1, label="x - y + 1 = 0")
plt.plot(xx, y2, label="3x + 2y - 12 = 0")

plt.plot(x.value, y.value, 'ro')
plt.text(x.value+0.1, y.value, f"({x.value}, {y.value})")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.title("Graph of Equations")

plt.savefig("/home/shriyasnh/Desktop/matgeonew/4.11.30/figs/equations_solution.png", dpi=300, bbox_inches="tight")
plt.show()
