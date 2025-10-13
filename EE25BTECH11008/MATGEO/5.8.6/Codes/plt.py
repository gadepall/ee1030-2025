import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 15, 400)
y1 = 3*x - 3
y2 = 4*x - 8

plt.figure(figsize=(8, 6))
plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='red')
plt.text(10, 20, r'$3x - y = 3$', color='blue', fontsize=12)
plt.text(7.5, 35, r'$4x - y = 8$', color='red', fontsize=12)
x_int = 5
y_int = 12
plt.scatter(x_int, y_int, color='green', s=50, zorder=5)
plt.text(x_int + 0.5, y_int-0.5, f'({x_int}, {y_int})', color='green', fontsize=12)

plt.title("Plot of the system of equations")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.show()
