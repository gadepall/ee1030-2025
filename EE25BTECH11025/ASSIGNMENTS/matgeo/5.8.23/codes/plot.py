import matplotlib.pyplot as plt
from call import get_data
import numpy as np

D, M, E, F = get_data()

x = np.linspace(-10, 10, 200)
y = ((M[0])/E[1]) - ((E[0]*x)/E[1])

X = np.linspace(-10, 10, 200)
Y = ((M[1])/F[1]) - ((F[0]*X)/F[1])

plt.plot(x, y, color = 'blue')
plt.plot(X, Y, color = 'blue')
plt.plot(D[0], D[1], 'ro')

plt.text(-6.37, 19.98, "3x+2y=21", fontsize = 10, color = 'black')
plt.text(-9.68, 13.94, "3x+4y=27", fontsize = 10, color = 'black')
plt.text(5.1, 3.1, "(5,3)", fontsize = 10, color = 'black')
plt.axvline(x=0, color = 'black', linewidth = 1)
plt.axhline(y = 0, color = 'black', linewidth = 1)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis("equal")
plt.grid(True)
plt.savefig('../figs/plot.png')
plt.show()