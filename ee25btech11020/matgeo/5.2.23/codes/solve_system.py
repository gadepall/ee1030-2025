import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./solve_system.so")

lib.solve_system.argtypes = [ctypes.c_double * 6,
                             ctypes.POINTER(ctypes.c_double),
                             ctypes.POINTER(ctypes.c_double)]

aug = (ctypes.c_double * 6)(3, -5, -4,
                            2,  3, 13)

x = ctypes.c_double()
y = ctypes.c_double()

lib.solve_system(aug, ctypes.byref(x), ctypes.byref(y))

print("Solution: x =", x.value, ", y =", y.value)

xx = np.linspace(-10, 10, 400)
y1 = (3*xx + 4)/5            # 3x - 5y = -4
y2 = (13 - 2*xx)/3           # 2x + 3y = 13

plt.figure(figsize=(6,6))
plt.plot(xx, y1, label="3x - 5y = -4")
plt.plot(xx, y2, label="2x + 3y = 13")
plt.text(5, (3*5+4)/5, "3x - 5y = -4", color="blue")
plt.text(5, (13-2*5)/3, "2x + 3y = 13", color="green")
plt.scatter([x.value], [y.value], color="red")
plt.text(x.value+0.2, y.value, f"({x.value:.2f}, {y.value:.2f})", color="red")

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True)
plt.savefig("../figs/img1")

