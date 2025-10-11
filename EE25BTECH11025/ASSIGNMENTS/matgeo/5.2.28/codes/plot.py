import matplotlib.pyplot as plt
import numpy as np
from call import get_data

C, D, E, F = get_data()

x = np.linspace(-10, 10, 100)
y = -((C[0]*x)-E)/D[0]

X = np.linspace(-15, 15, 100)
Y = -((C[0]*X)-E)/D[0]

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