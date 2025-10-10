import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = (5/8)*x + (1/8)

X = np.linspace(-15, 15, 100)
Y = (5/8)*X + (1/8)

plt.plot(X, Y, '-k')
plt.plot(x, y, '-r')

plt.text(-13.64, -8.96, r'$5x-8y=-1$', fontsize=10, color='black')
plt.text(1.06, 1.08, r'$3x-\frac{24}{5}y=-\frac{3}{5}$', fontsize=10, color='black')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.grid(True)
plt.savefig("../figs/plot.png")
plt.show()