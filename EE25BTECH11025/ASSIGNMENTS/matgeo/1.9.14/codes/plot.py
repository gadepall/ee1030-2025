import numpy as np
import matplotlib.pyplot as plt
from call import get_data

Px, Py, Qx, Qy, Rx, Ry, Mx, My, values = get_data()

a = ([Px, Qx, Rx, Mx, Px, Rx])
b = ([Py, Qy, Ry, My, Py, Ry])

plt.plot(a, b, color = 'black')

plt.text(Px, Py, 'P', fontsize=12, color = 'red')
plt.text(-4.4, -3.9, 'Q', fontsize=12, color = 'red')
plt.text(Rx, Ry, 'R', fontsize=12, color = 'red')
plt.text(-1.1, -0.8, 'M', fontsize=12, color = 'red')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.grid(True)
plt.savefig('../figs/plot.png')
plt.show()

