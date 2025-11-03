import numpy as np
import matplotlib.pyplot as plt

V = np.array([[1, 0], [0, 0]])
u = np.array([[0], [-8]])
f = 0
m = np.array([[1], [np.sqrt(3)]])
x = 8 * np.sqrt(3)
y = x**2 / 16
q = np.array([x, y])
K = y - np.sqrt(3) * x
x_vals = np.linspace(-50, 50, 400)
y_parabola = x_vals**2/16
y_line = np.sqrt(3)*x_vals + K
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_parabola, label=r'$x^2 = 16y$', color='blue')
plt.plot(x_vals, y_line, label=rf'$y = \sqrt{{3}}x {K:.0f}$', color='red', linestyle='--')
plt.plot(q[0], q[1], 'ko', label='Point of Contact')
plt.text(q[0], q[1], f'({q[0]:.2f}, {q[1]:.2f})')
plt.title("Parabola and Tangent Line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/10.3.12/figs/Figure_1.png")
plt.show()
