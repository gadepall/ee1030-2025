import numpy as np
import matplotlib.pyplot as plt
import ctypes

solve = ctypes.CDLL('./solve.so')

solve.function.argtypes = [
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
solve.function.restype = None

def get_roots_from_c(a, b, c):
    root1_c = ctypes.c_double(0)
    root2_c = ctypes.c_double(0)
    solve.function(a, b, c, ctypes.byref(root1_c), ctypes.byref(root2_c))
    return root1_c.value, root2_c.value

p_val = 3.0

a, b, c = p_val, -14.0, 8.0
root1, root2 = get_roots_from_c(a, b, c)

if np.isclose(root2, 6 * root1):
    print("The second root is six times the first root.")
else:
    print("The given value of p is wrong.")

x = np.linspace(-1/3, 5, 200)
y = p_val * x**2 - 14 * x + 8
roots = [root1, root2]

plt.figure(figsize=(10, 8))
plt.plot(x, y, label=fr'Parabola: $y = {p_val:.0f}x^2 - 14x + 8$')
plt.axvline(color='black')
plt.axhline(0, color='black', linestyle='-', label=r'Line: $y=0$')

plt.plot(roots, [0, 0], 'ro', markersize=6, label=fr'Roots at x={root1:.2f} and x={root2:.2f}')
plt.text(root1, -1, f'{root1:.2f}', ha='center')
plt.text(root2, -1, f'{root2:.2f}', ha='center')

plt.title(f'Solution for p = {p_val:.0f}')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.legend()
plt.savefig("../figs/plot_c.jpg")
plt.show()
