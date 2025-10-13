import numpy as np
import matplotlib.pyplot as plt

p_val = 3.0

coeffs = [p_val, -14, 8]
roots = np.roots(coeffs)
root1, root2 = np.sort(roots)

if np.isclose(root2, 6 * root1):
    print("The second root is six times the first root.")
else:
    print("The given value of p is wrong.")

x = np.linspace(-1/3, 5, 200)
y = p_val * x**2 - 14 * x + 8

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
plt.savefig("../figs/plot_p.jpg")
plt.show()
